This repo holds the source files for *The Open Quran*, along with
[an AST for each surah][1], serialised with JSON, and a script for
generating the JSON files whenever the source files are edited.

*The Open Quran* is an English translation of the Quran. It is derived
from *The Message*, a translation developed by a community of Islamic
reformists based at [free-minds.org][2], led by Layth Saleh al-Shaiban.

The aim of this project is to:

- Generally improve the situation by moving everything to GitHub.
- Format the source so it is easy to automatically parse the translation.
- Make the translation available as JSON AST files. Other people can then use
  them to generate pretty webpages, apps, ebooks etc.

To improve the readability of the translation, we will use paragraphs and
ignore indexing. Indexing is retained in the source code, but the English
is written so that the indexing could be hided by software, and the text
will flow as natural English, in paragraphs. Software can use the JSON
AST files to generate ebooks with or without indexing, and apps can
allow the user to toggle indexing on and off. It will be nice to
be able to read a translation of the Quran without the message
being broken into verses which were not in the revelation.

The contents of the repo are in the public domain.

[1]: https://github.com/carlsmith/quran/tree/master/json
[2]: http://www.free-minds.org
