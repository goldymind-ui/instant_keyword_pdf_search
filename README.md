# instant_keyword_pdf_search
Lightning-fast offline search through thousands of teaching PDFs, journals and magazines via a local web interface.
<img width="592" height="255" alt="image" src="https://github.com/user-attachments/assets/1e60b731-ab11-496e-9b2b-34b5daad8d2f" />

# PDF Library Search

Lightning-fast offline search through thousands of PDFs via a local web interface.

## Features

* Searches thousands of PDFs in seconds
* Works completely offline
* Click search results to open PDFs
* Opens PDFs directly on the matching page
* No subscription
* No search limits

## Requirements

* Python 3
* Flask
* PyMuPDF

## Installation

Install the required packages:

```bash
pip install flask pymupdf
```

## Configuration

Edit the following paths in `web_search.py` and `build_db.py`:

* PDF folder location
* Foxit PDF Reader location

## Building the Index

Run:

```bash
python build_db.py
```

This creates `library.db`, a searchable database of all PDFs.

## Starting the Search Engine

Run:

```bash
python web_search.py
```

Open:

http://127.0.0.1:5000

in your browser.

## Updating the Library

When new PDFs are added, rebuild the database:

```bash
python build_db.py
```

## Notes

* Text-based PDFs are supported.
* OCR support for scanned PDFs is planned.
* Tested with Foxit PDF Reader.
