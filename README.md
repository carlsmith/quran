# The Open Quran

*The Open Quran* project develops open source resources for publishing
modern translations of the Quran. This repo includes:

- A modern translation of the Quran, formatted
  to make it easy to maintain, and easy to parse.
- Software for parsing the source files into JSON AST files.
- Software for generating editions of the translation in various
  formats (currently, only HTML is supported).

## Status

The project is just getting started. There is plenty that people can help
with, but nothing is ready to start using properly yet. If you would like
to get involved at all, there is [an open issue][1] for people to use to
introduce themselves.

The software in this repo will generate a pretty HTML version of the
translation every time `update.py` is executed. However, until a surah
is divided into paragraphs, it will render as a wall of text. Adding
paragraphs is the most important thing to get done at the moment.

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
  (indexing is kept in the source and ASTs to make it optional for readers).
- Bring people together.

[1]: https://github.com/carlsmith/quran/issues/1
[2]: http://www.free-minds.org
