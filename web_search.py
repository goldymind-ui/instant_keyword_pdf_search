from flask import Flask, request
import sqlite3
import subprocess
import os

app = Flask(**name**)

# CHANGE THESE PATHS

PDF_FOLDER = r"PATH_TO_YOUR_PDFS"
FOXIT = r"PATH_TO_FOXITPDFREADER.EXE"

@app.route("/open")
def open_pdf():

```
filename = request.args.get("file")
page = request.args.get("page", "1")

if filename:

    pdf_path = os.path.join(PDF_FOLDER, filename)

    subprocess.Popen([
        FOXIT,
        "/A",
        f"page={page}",
        pdf_path
    ])

return """
<html>
<body>
<script>
window.history.back();
</script>
</body>
</html>
"""
```

@app.route("/", methods=["GET"])
def search():

```
query = request.args.get("q", "")

html = f"""
<html>
<body>

<h1>PDF Search</h1>

<form>
    <input name="q" value="{query}" size="50">
    <input type="submit" value="Search">
</form>

<hr>
"""

if query:

    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    cur.execute(
        """
        SELECT file, page
        FROM pages
        WHERE pages MATCH ?
        LIMIT 100
        """,
        (query,)
    )

    results = cur.fetchall()

    conn.close()

    html += f"<h2>{len(results)} results</h2>"

    for file, page in results:

        html += f"""
        <p>
        <a href="/open?file={file}&page={page}">
        <b>{file}</b>
        </a><br>
        Page {page}
        </p>
        """

html += """
</body>
</html>
"""

return html
```

app.run(host="127.0.0.1", port=5000)
