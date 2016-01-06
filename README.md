# The Open Quran Project

*The Open Quran Project* (OQ) publishes digital editions of the Quran - along
with all of our resources - under permissive licensing.

## Contents

This repo currently includes:

- A Quran translation, formatted using Text, our own simple markup language.
- A (Python 2) Text parser that can parse a Text file to produce a JSON AST.
- A complete, up-to-date set of JSON AST files.

There is also library (`html`) for generating an edition of the translation
in HTML. It is currently pretty basic, and is just used internally to pretty
print the translation, to check everything is working correctly, and to make
it easier to read the text. We host [a copy of the output][3] online.

## The Translation

The translation used in this project is derived from *The Message*, an original
translation, developed by Layth Saleh al-Shaiban and a community of Islamic
reformists, based at [free-minds.org][2].

We used *The Message* because:

- It is an excellent translation, with nice, modern English.
- It is a direct translation. It is not contextualised by hadith according to
  one or another school of thought.
- The translation was developed online, by the community, so its authors are
  essentially an open source community already.
- The work is not encumbered by copyright.

Our fork of the translation does things a bit differently with the way the
English is structured. Other translations structure sentences according to
where verses begin and end. Instead, we join verses together to form more
natural English sentences, and then group the sentences into paragraphs.

The indexing (chapter and verse numbering) is retained in the source code,
and the JSON ASTs, so different software can render it in different ways.

Indexing is really helpful, of course, but it is also really  helpful to be
able to render the text of the translation without any indexing, so that it
looks and reads just like poetry.

## The Project

The primary purpose of OQ is to publish editions of the translation in popular
formats. Another important goal is to make it easy for people to use the same
resources to create third-party, custom editions of the translation, as
books, ebooks, websites or applicatons.

### Text

Text is a simple markup language that is designed to mark up scripture. Each
chapter has its own file. Each file contains one or more paragraphs, which are
delimited by putting an empty line between them. Each paragraph contains one
or more verses, which are delimited by *index marks*.

Index marks are contained by square brackets (`[]`). They contain two
integers, separated by a colon (`:`). The first is the chapter, the
second is the verse. For example `[22:4]`.

An example of a Text document (Quran, Surah 1):

``` text
[1:1] In the name of God, the Almighty, the Merciful.

[1:2] Praise be to God, Lord of the worlds, [1:3] the Almighty, the Merciful,
[1:4] Sovereign of the Day of Recompense. [1:5] You alone we serve, and to
You alone do we turn to for help. [1:6] Guide us to the straight path,
[1:7] the path of those who You have blessed, not that of those who
have incurred the wrath, nor the misguided.
```

The first surah in [the online demo][3] is an example of one way the Text
document above can be automatically rendered.

## Status

The project is just getting started. There are plenty of things people can
help with, but nothing is ready to start using properly yet. If you would
like to get involved, there is [an open issue][1] for people to introduce
themselves.

Until a surah is divided into paragraphs, it will render as a wall of text.
Adding paragraphs is the most important thing to get done at the moment.
Things can always be improved, but surahs 1 and 107-114 are ready to use.
The rest of the surahs are still as they were when they were scraped from
free-minds.org.

Once the surahs have been divided into paragraphs, the next big issue will
be improving the software that generates HTML editions. From there on in,
everything should be fairly optional and can be worked on as and when.

The software that exists so far does everything we need it to do at this
stage. Each time `update.py` is executed, the JSON files in `/json` will
be updated, then `/html/book.html` will be updated too.

Do not forget to [say hello][1].

[1]: https://github.com/carlsmith/quran/issues/1
[2]: http://www.free-minds.org
[3]: http://carlsmith.github.io/quran
[4]: http://www.free-minds.org/quran
[5]: https://github.com/carlsmith/quran/blob/master/source/surah1.text
