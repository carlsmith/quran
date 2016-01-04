import os, sys, json

def make_template():

    with open("html/template.html") as file:

        html = file.read()
        html = html.replace("<stylesheet>", open("html/style.css").read())
        return html.replace("<javascript>", open("html/script.js").read())

def generate(template=None, output_path="html/book.html"):

    main = ["<main>"]
    push = main.append
    span = '<span title="Surah {1}, Verse {2}">{0}</span>'

    if not template: template = make_template()

    for index in range(1, 115):

        path = os.path.join("json/surah{}.json".format(index))
        with open(path) as file: data = json.loads(file.read())

        push('<section id="surah{}">'.format(index))

        for paragraph in data:

            push("<p>")

            for line in paragraph:
                
                push(span.format(line["quran"], line["surah"], line["verse"]))

            push("</p>")

        push("</section>")

    push("</main>")

    document = template.replace("<document>", "\n".join(main))

    if output_path:

        with open(output_path, "w") as book: book.write(document)

    return document
