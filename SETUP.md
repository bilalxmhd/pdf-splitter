# PDF Splitter - Flask Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Flask App

```bash
python app.py
```

### 3. Open Browser

Navigate to: **http://localhost:5000**

---

## How It Works

### Architecture

- **Backend**: Flask server (`app.py`)
  - Handles file uploads
  - Processes PDF splitting using PyPDF
  - Serves split PDFs for download

- **Frontend**: HTML/JavaScript UI (`pdf_splitter_ui_flask.html`)
  - File upload with drag-and-drop
  - Settings for chunk size and prefix
  - Progress tracking
  - Download links

### API Endpoints

#### POST `/api/split`

Splits a PDF file.

**Request:**

- `file` (multipart/form-data): PDF file
- `chunk_size` (integer): Pages per chunk
- `prefix` (string): Output file prefix

**Response:**

```json
{
  "success": true,
  "total_pages": 100,
  "num_chunks": 10,
  "prefix": "invoice",
  "files": [
    { "name": "invoice_001.pdf", "pages": "1–10" },
    { "name": "invoice_002.pdf", "pages": "11–20" }
  ]
}
```

#### GET `/api/download/<filename>`

Downloads a split PDF file.

---

## Features

✅ Drag & drop PDF upload
✅ Customizable chunk size and output prefix
✅ Real-time progress tracking
✅ Secure file handling
✅ Up to 100MB file size limit
✅ Beautiful modern UI

---

## Folder Structure

```
pdf splitter/
├── app.py                          # Flask application
├── pdf_splitter_ui_flask.html      # Frontend UI
├── requirements.txt                # Python dependencies
├── input_files/                    # Temporary upload location
├── output_files/                   # Split PDFs storage
└── SETUP.md                        # This file
```

---

## Customization

### Change Port

Edit `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change 5000 to your port
```

### Change Upload Folder

Edit `app.py`:

```python
UPLOAD_FOLDER = 'path/to/uploads'
OUTPUT_FOLDER = 'path/to/outputs'
```

### Disable Debug Mode (Production)

Edit `app.py`:

```python
app.run(debug=False, port=5000)
```

---

## Troubleshooting

### Port Already in Use

If port 5000 is busy, change it in `app.py` or kill the process:

```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### PyPDF Import Error

Reinstall PyPDF:

```bash
pip uninstall pypdf
pip install pypdf
```

### Large File Upload Issues

Edit `app.py` to increase max file size:

```python
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB
```
