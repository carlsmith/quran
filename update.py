import os, sys, json, time, datetime
from html import book
from tell import tell

def last_modified(path):

    """This function takes a path to a file, and returns the last
    modified date. It is used by `update_json` to know which files
    have been modified since the last time it was called."""

    date = os.path.getmtime(path)
    date = datetime.datetime.fromtimestamp(date)
    return time.mktime(date.timetuple())

def update_timestamp():

    """This function updates the timestamp (stored in a file named
    timestamp.data), then returns the old timestamp. It is used by
    `update_json` to know which files have been modified since the
    last time `update_json` was called."""

    with open("timestamp.data", "r+") as file:

        old = float(file.read())

        now = datetime.datetime.now()
        now = time.mktime(now.timetuple())

        file.seek(0)
        file.write(str(now))
        file.truncate()

        return old

def parse(source):

    """This function parses a string of source, and returns a JSON AST,
    as a hash. It breaks the source into a list of blocks, which are
    paragraphs. Each block contains one or more verses.
    """

    def blockify(source):

        """This is the first step, where the source is broken into blocks.
        The output is a list of strings; each string is a block. Internal
        newlines are removed in the process."""

        blocks = [""]

        for line in source.split("\n"):

            line = line.strip()

            if line: blocks[-1] += line + " "
            elif blocks[-1]: blocks.append("")

        return [ block for block in blocks if block ]

    def subparse(block):

        """This function parses a single block of source, as returned by
        blockify. It finds the verses, and creates an AST that represents
        one paragraph in the translation.
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

    """This function cycles through the 115 source files, looking for the
    ones that have been modified since the last time it was executed. The
    function updates the JSON where necessary to keep all the input and
    output files in sync."""

    surahs_modified = 0
    last_update = update_timestamp()

    if shell: tell.info("Updating JSON AST files.")

    for surah in range(1, 115):

        source_path = "source/surah{}.text".format(surah)

        if last_modified(source_path) > last_update:

            if shell:

                tell.info("Rebuilding Surah {}.".format(surah))
                surahs_modified += 1

            with open(source_path) as source_file:

                with open("json/surah{}.json".format(surah), "w") as json_file:

                    data = parse(source_file.read())
                    json_file.write(json.dumps(data))

    if shell:

        if surahs_modified: tell.done("The JSON files are now up to date.")
        else: tell.info("No edits were found in the source files.")

    return surahs_modified

def update_book(shell=False):

    tell.info("Rebuilding the HTML book.")
    book.generate()
    tell.done("HTML book updated.")

if __name__ == "__main__":

    try: arg = sys.argv[1]
    except IndexError: arg = None

    if arg is None:

        if update_json(True): update_book(True)

    elif arg == "json": update_json(True)
    elif arg == "book": update_book(True)
    else:

        tell.fail("Unrecognised arguments: `{}`".format(sys.argv[1:]))
        tell.info("The valid arguments are `json` or `book`.")
        tell.fail("Update failed.")
        sys.exit()

    tell.done("Update complete.")
