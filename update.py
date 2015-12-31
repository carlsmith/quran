import os
import json
import time
import datetime

def last_modified(path):

    date = os.path.getmtime(path)
    date = datetime.datetime.fromtimestamp(date)
    return time.mktime(date.timetuple())

def update_timestamp():

    with open("timestamp.data", "r+") as file:

        old = float(file.read())

        now = datetime.datetime.now()
        now = time.mktime(now.timetuple())

        file.seek(0)
        file.write(str(now))
        file.truncate()

        return old

def parse(source):

    def blockify(source):

        blocks = [""]

        for line in source.split("\n"):

            line = line.strip()

            if line: blocks[-1] += line + " "
            elif blocks[-1]: blocks.append("")

        return [ block for block in blocks if block ]

    def subparse(block):

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

def update_files():

    last_update = update_timestamp()

    for surah in range(1, 115):

        source_path = "source/surah{}.text".format(surah)

        if last_modified(source_path) > last_update:

            if __name__ == "__main__": print "Rebuilding Surah: ", surah

            with open(source_path) as source_file:

                with open("json/surah{}.json".format(surah), "w") as json_file:

                    data = parse(source_file.read())
                    json_file.write(json.dumps(data))

if __name__ == "__main__": update_files()
