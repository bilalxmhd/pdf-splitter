from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from pypdf import PdfReader, PdfWriter
import os
import re
from io import BytesIO

app = Flask(__name__, template_folder='.', static_folder='.')

UPLOAD_FOLDER = 'input_files'
OUTPUT_FOLDER = 'output_files'
ALLOWED_EXTENSIONS = {'pdf'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size


def sanitize_prefix(raw):
    raw = raw.strip()
    raw = re.sub(r'[\/\\:*?"<>|]', '-', raw)
    raw = re.sub(r'\s+', '_', raw)
    return raw or 'output'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('pdf_splitter_ui_flask.html')


@app.route('/api/split', methods=['POST'])
def split_pdf():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        chunk_size = int(request.form.get('chunk_size', 1))
        prefix = request.form.get('prefix', 'output')

        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if not allowed_file(file.filename):
            return jsonify({'error': 'Only PDF files allowed'}), 400

        prefix = sanitize_prefix(prefix)

        # Read PDF
        pdf_data = file.read()
        pdf_reader = PdfReader(BytesIO(pdf_data))
        total_pages = len(pdf_reader.pages)

        if total_pages == 0:
            return jsonify({'error': 'PDF has no pages'}), 400

        num_chunks = (total_pages + chunk_size - 1) // chunk_size
        output_files = []

        # Process chunks
        for i in range(num_chunks):
            start_page = i * chunk_size
            end_page = min(start_page + chunk_size, total_pages)

            pdf_writer = PdfWriter()
            for j in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[j])

            output_filename = f"{prefix}_{str(i + 1).zfill(3)}.pdf"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)

            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            output_files.append({
                'name': output_filename,
                'pages': f"{start_page + 1}–{end_page}"
            })

        return jsonify({
            'success': True,
            'total_pages': total_pages,
            'num_chunks': num_chunks,
            'prefix': prefix,
            'files': output_files
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/download/<filename>')
def download_file(filename):
    try:
        filename = secure_filename(filename)
        file_path = os.path.join(OUTPUT_FOLDER, filename)

        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404

        return send_file(file_path, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
