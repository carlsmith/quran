import json

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

for surah in range(1, 115):

    with open("source/surah{}.text".format(surah)) as source_file:

        with open("data/surah{}.json".format(surah), "w") as output_file:

            data = parse(source_file.read())
            data = json.dumps(data)
            output_file.write(data)
