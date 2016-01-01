# The Open Quran

*The Open Quran* project develops open source resources for publishing
modern translations of the Quran. This repo includes:

- A modern translation of the Quran, formatted
  to make it easy to maintain, and easy to parse.
- Software for parsing the source files into JSON AST files.
- Software for generating editions of the translation in various
  formats, like HTML, EPUB and PDF.

## Status

The project is just getting started. There is plenty that people can help
with, but nothing is ready to start using properly yet. Open an Issue if
you want to introduce yourself. Treat the Issue tracker as a forum.

The software will generate a pretty HTML version of the translation every
time `update.py` is executed, but until each surah is divided into paragraphs,
they will render as walls of text. Adding paragraphs is the most important
thing to get done at the moment.

Once the surahs have been divided into paragraphs, the most pressing issue
will be improving the software that generates HTML editions. From there on
in, everything should be fairly optional and can be worked on as and when.

## Translation

The Quran translation used in this project is derived from *The Message*, an
original translation that was developed by a community of Islamic reformists
based at [free-minds.org][2]. Layth Saleh al-Shaiban led the translation.

## The Project

The aim of this project is to:

- Generally improve the situation by moving everything to GitHub.
- Format the source so it is easy to automatically parse the translation.
- Make the translation available as JSON AST files for generating editons from.
- Develop software for generating editions in various formats.
- Improve readability by using paragraphs and ignoring indexing in the English
  (though indexing will be retained in the source and ASTs to make it optional
  for end users).

[1]: https://github.com/carlsmith/quran/tree/master/json
[2]: http://www.free-minds.org
