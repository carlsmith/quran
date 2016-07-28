""" Update Script
============================================================ OQ == GPL3 2016 ==

When using this (currently limited) toolset from the command line, you will
always run this file as the top-level script. Its job is converting the
translation source code into HTML (and other formats eventually).

The overall process has three stages. There are 114 (one pre surah) source
files, which are edited by hand, and use a simple markup format. They are
parsed into JSON AST structs that are written to 114 JSON text files. The
single HTML page (index.html) is generated from those JSON files.

    114 source files -> 114 JSON AST files -> 1 HTML file

Other output formats will be added once the translation is complete.

You can currently do three things with this script:

    1: $ python update.py json
    2: $ python update.py book
    3: $ python update.py

Case 1 updates the JSON, Case 2 updates the HTML, and Case 3 updates both the
JSON and the HTML.

In case 1 and 2, the script only updates the JSON for source files that have
been edited since the last time the script was executed. In case 1 and 3, the
HTML is is regenerated from scratch, based on the current state of the JSON
AST files."""

import os, sys, json, time, datetime
from tell import tell
from html import update as html

def last_modified(path):

    """This function takes a path to a file, and returns the date that it was
    last modified. This function is used by `update_json` to know which files
    have been modified since the last time it was called."""

    date = os.path.getmtime(path)
    date = datetime.datetime.fromtimestamp(date)
    return time.mktime(date.timetuple())

def update_timestamp():

    """This function updates the timestamp, which is stored in a file named
    timestamp.data, then returns the old timestamp. It is used by `update_json`
    to know which files have been modified since the last time `update_json`
    was called."""

    with open("timestamp.data", "r+") as file:
        old = float(file.read())
        now = time.mktime(datetime.datetime.now().timetuple())
        file.seek(0)
        file.write(str(now))
        file.truncate()
        return old

def parse(source):

    """This function parses a string of source - the content from a source
    file - which represents a surah. The function returns an AST for the
    surah. The AST for each surah is structured as a list of paragraphs,
    and each paragraph is structured as a list of verses. Each verse is
    a hash with three properties:

        quran: String # the text of the verse (with one trailing space)
        surah: Number # the surah number
        verse: Number # the verse number

    Note: The unindexed Bismillahs have `0` for their `verse` property."""

    def blockify(source):

        """This is the first step, where the source is broken into paragraphs,
        based on blank lines in the source. The output is a list of strings.
        Each string is a paragraph. Newlines (with any trailing whitespace)
        inside paragraphs are converted to single spaces."""

        paragraphs = [""]
        for line in source.strip().split("\n"):
            line = line.strip()
            if line: paragraphs[-1] += line + " "
            elif paragraphs[-1]: paragraphs.append("")

        return paragraphs

    def subparse(block):

        """This function parses a single paragraph of source, as returned by
        the `blockify` function. This finds the individual verses within the
        given paragraph. It returns an AST for the paragraph, as previously
        described.

        TODO: Validate the input based on the AST.
        """

        verses = []
        context = None
        for char in block:

            if char == "[":
                if verses: verses[-1]["quran"] = verses[-1]["quran"].strip()
                verses.append({"surah": "", "verse": "", "quran": ""})
                context = "surah"
            elif char == ":" and context == "surah":
                verses[-1]["surah"] = int(verses[-1]["surah"])
                context = "verse"
            elif char == "]":
                verses[-1]["verse"] = int(verses[-1]["verse"])
                context = "quran"
            else: verses[-1][context] += char

        verses[-1]["quran"] = verses[-1]["quran"].strip()
        return verses

    return [ subparse(block) for block in blockify(source) ]

def update_json(shell=False):

    """This function cycles through the 114 source files, looking for any
    that have been modified since the last time it was executed. The function
    updates the JSON where necessary to bring the JSON AST files into sync
    with the source."""

    surahs_modified = 0
    last_update = update_timestamp()
    if shell: tell.info("Updating JSON AST files.")

    for surah in range(1, 115):

        source_path = "source/surah{}.text".format(surah)

        if last_modified(source_path) > last_update:

            if shell:
                tell.info("Rebuilding Surah `{}`.".format(surah))
                surahs_modified += 1

            with open(source_path) as source_file:
                with open("json/surah{}.json".format(surah), "w") as json_file:
                    data = parse(source_file.read())
                    json_file.write(json.dumps(data))

    if shell:
        if surahs_modified: tell.done("The JSON files are now up to date.")
        else: tell.info("No edits were found in the source files.")

    return surahs_modified

def update_html(shell=False):

    """The function regenerates the HTML version of the translation. It
    assumes the JSON is upto date."""

    if shell: tell.info("Rendering the HTML.")
    html.generate()
    if shell: tell.done("Updated `html/index.html`.")

if __name__ == "__main__":

    try: arg = sys.argv[1]
    except IndexError: arg = None

    if arg is None: update_json(True) and update_html(True)
    elif arg == "json": update_json(True)
    elif arg == "book": update_html(True)
    else:

        tell.fail("Unrecognised arguments: `{}`".format(sys.argv[1:]))
        tell.info("The valid arguments are `json` or `book`.")
        tell.fail("Update failed.")
        sys.exit()

    tell.done("Update complete.")
