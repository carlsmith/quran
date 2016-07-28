The script named `update.py` reads from `template.html`, `style.css` and
`script.js`, and uses them to create a HTML page. The entire translation
is interpolated into the HTML, populated surah by surah, using the JSON
AST files. The output is a single webpage, which is saved as `index.html`.

In practice, `update.py` is normally imported and used by a script that is
also named `update.py` that lives in the root directory. That script will
check the source for modifications, updating any JSON AST files that are
out of date, before generating the HTML. That script provides a more
user-friendly interface to the OQ toolkit.
