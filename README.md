# 📄 PDF Splitter

A simple yet powerful web-based tool to split PDF files into smaller chunks. Built with Flask and PyPDF, it provides a user-friendly interface for breaking down large PDFs into manageable pieces.

## ✨ Features

- 🎯 **Drag & Drop Upload** - Easily upload PDFs with intuitive drag-and-drop interface
- 📏 **Customizable Chunk Size** - Split PDFs by number of pages per chunk
- 🏷️ **Custom Naming** - Add prefixes to output files for better organization
- 📊 **Real-time Progress** - Track splitting progress with instant feedback
- 🔒 **Secure File Handling** - Files are processed server-side with proper validation
- 💾 **Batch Download** - Download all split PDFs at once
- 🎨 **Modern UI** - Clean, responsive web interface
- 📈 **Large File Support** - Handles PDFs up to 100MB

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**

```bash
cd pdf-splitter
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python app.py
```

The application will start at **http://localhost:5000**

Open your browser and navigate to the URL. You're ready to split PDFs!

## 📖 Usage

1. **Upload PDF** - Drag and drop or click to select a PDF file
2. **Set Chunk Size** - Enter the number of pages per split file (default: 1)
3. **Add Prefix** - Optional prefix for output files (e.g., "invoice" → "invoice_001.pdf")
4. **Click Split** - Process the PDF
5. **Download** - Download individual files or all at once

### Example

If you upload a 100-page PDF with:

- Chunk size: 10
- Prefix: "report"

You'll get 10 files:

- `report_001.pdf` (pages 1-10)
- `report_002.pdf` (pages 11-20)
- ... and so on

## 🏗️ Project Structure

```
pdf-splitter/
├── app.py                          # Flask backend server
├── split_pdftool.py                # PDF splitting utility module
├── pdf_splitter_ui_flask.html      # Frontend web interface
├── requirements.txt                # Python dependencies
├── SETUP.md                        # Setup guide
├── README.md                       # This file
├── input_files/                    # Temporary upload directory
├── output_files/                   # Split PDFs output directory
└── newEnv/                         # Virtual environment (optional)
```

## 🔧 Configuration

### Change Port

Edit `app.py` and modify the port number:

```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change 5000 to desired port
```

### Customize Upload Folder

Edit `app.py`:

```python
UPLOAD_FOLDER = 'path/to/uploads'
OUTPUT_FOLDER = 'path/to/outputs'
```

### Increase File Size Limit

Edit `app.py`:

```python
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB limit
```

### Disable Debug Mode (Production)

Edit `app.py`:

```python
app.run(debug=False, port=5000)
```

## 🌐 API Endpoints

### POST `/api/split`

Splits a PDF file based on specified parameters.

**Request:**

- `file` (multipart/form-data): PDF file to split
- `chunk_size` (integer): Number of pages per chunk
- `prefix` (string): Prefix for output filenames

**Response:**

```json
{
  "success": true,
  "total_pages": 100,
  "num_chunks": 10,
  "prefix": "invoice",
  "files": [
    { "name": "invoice_001.pdf", "pages": "1–10" },
    { "name": "invoice_002.pdf", "pages": "11–20" },
    ...
  ]
}
```

### GET `/api/download/<filename>`

Downloads a specific split PDF file.

**Parameters:**

- `filename` (string): Name of the file to download

**Response:** PDF file attachment

## 📋 Requirements

```
Flask==2.3.3
Werkzeug==2.3.7
pypdf==6.12.2
```

## 🐛 Troubleshooting

### Port Already in Use

If port 5000 is already in use:

**Windows:**

```bash
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**macOS/Linux:**

```bash
lsof -i :5000
kill -9 <PID>
```

Or simply change the port in `app.py`.

### PyPDF Import Error

Reinstall PyPDF:

```bash
pip uninstall pypdf
pip install pypdf
```

### Large File Upload Issues

Increase the max file size limit in `app.py`:

```python
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB
```

### Files Not Found After Split

Ensure `input_files/` and `output_files/` directories exist with proper permissions:

```bash
mkdir input_files
mkdir output_files
```

## 🔒 Security Features

- ✅ File type validation (PDF only)
- ✅ Filename sanitization to prevent directory traversal attacks
- ✅ Secure file handling using Werkzeug
- ✅ File size limits
- ✅ Input validation on all user inputs

## 💡 Tips & Best Practices

1. **Organize Output** - Use descriptive prefixes to organize split files by document type or date
2. **Batch Processing** - For large PDFs, use moderate chunk sizes (5-20 pages) for faster processing
3. **File Cleanup** - Periodically clean up the `output_files/` directory to save disk space
4. **Backup Original** - Keep a backup of original PDFs before splitting

## 🤝 Contributing

Found a bug or have a feature request? Feel free to open an issue or submit a pull request.

## 📝 License

This project is open source and available under the MIT License.

## 📞 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Happy PDF Splitting!** 🎉

Made with ❤️ using Flask and PyPDF
