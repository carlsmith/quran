The script named `book.py` takes `template.html`, `style.css` and `script.js`,
and uses them to create a HTML page that contains the entire translation,
populated with surahs using the JSON AST files. The output is a single
webpage, which is saved as `book.html`.

In practice, `book.py` is normally imported and used by `update.py` in the
root directory. That script will check for source code files that have been
modified, and parse them to update the JSON ASTs, before generating the HTML.
