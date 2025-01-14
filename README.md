# pdf2txt
Easily and quickly convert PDF documents to plain text (.txt) files.

## Description
This tool provides a straightforward way to extract text content from PDF files and save it to a text file. It processes all pages of the PDF and maintains the text structure.

## Features
- Converts PDF files to plain text
- Handles multiple pages
- UTF-8 encoding support
- Simple error handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf-to-text-converter.git
cd pdf-to-text-converter
```

2. Install the required dependency:
```bash
pip install PyPDF2
```

```python
from pdf2txt import pdf_to_text
pdf_to_text("input.pdf", "output.txt")
```

### 2. As a standalone script
```python
python pdf2txt.py
```

By default, the script will look for a file named "2501.00663v1.pdf" and output to "output.txt". You can modify these paths in the script.

## Error Handling
The script includes basic error handling and will display an error message if:
- The PDF file cannot be found
- The output location is not writable
- The PDF is corrupted or cannot be read

## License
This project is open source and available under the MIT License.

## Author
[Caleb Palmquist](https://x.com/PalmquistCaleb)

## Acknowledgments
- PyPDF2 library and its contributors
