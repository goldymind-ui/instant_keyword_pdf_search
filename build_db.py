import fitz
import sqlite3
import os

# CHANGE THIS TO YOUR PDF FOLDER

PDF_FOLDER = r"PATH_TO_YOUR_PDFS"

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS pages
USING fts5(
file,
page,
text
)
""")

pdf_files = [
f for f in os.listdir(PDF_FOLDER)
if f.lower().endswith(".pdf")
]

for pdf_name in pdf_files:

```
pdf_path = os.path.join(PDF_FOLDER, pdf_name)

print("Indexing:", pdf_name)

try:

    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):

        text = doc[page_num].get_text()

        if text.strip():

            cur.execute(
                """
                INSERT INTO pages
                (file, page, text)
                VALUES (?, ?, ?)
                """,
                (
                    pdf_name,
                    page_num + 1,
                    text
                )
            )

    conn.commit()
    doc.close()

except Exception as e:

    print("ERROR:", pdf_name, e)
```

conn.close()

print()
print("Finished.")
