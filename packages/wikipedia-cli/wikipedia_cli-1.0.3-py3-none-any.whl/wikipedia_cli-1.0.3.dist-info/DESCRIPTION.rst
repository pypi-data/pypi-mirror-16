Wikipedia-cli
=============

A command-line interface for fetching summaries of Wikipedia pages. It is built
over Jonathan Goldsmith's
`wikipedia library <https://github.com/goldsmith/Wikipedia>`__.


Takes a query to Wikipedia as an argument and an optional language flag.

Installation
------------

The program is available on
`pypi <https://pypi.python.org/pypi/wikipedia-cli>`__,
so you can just run::

    $ pip install wikipedia-cli

Examples
--------

The language default is English::

    $ wikipedia helsinki

    Helsinki

    Helsinki (/hɛlˈsɪŋki/; Finnish pronunciation: [ˈhelsiŋki]; Swedish:
    Helsingfors) is the capital and largest city of Finland. It is in the
    ...
    and worst cities to live in globally, Helsinki placed among the
    world's top ten cities.

    https://en.wikipedia.org/wiki/Helsinki

    Open URL (y/n)?

The desired language is specified with the ``-l`` flag::

    $ wikipedia -l fi helsinki

    Helsinki

    Helsinki (ruots. Helsingfors) on Suomen pääkaupunki ja Uudenmaan
    maakuntakeskus. Se sijaitsee Suomenlahden pohjoisrannalla Uudenmaan
    ...
    vuonna 1640. Helsingistä tuli Suomen suuriruhtinaskunnan pääkaupunki
    vuonna 1812 ja Suomen pääkaupunki maan itsenäistyessä vuonna 1917.

    https://fi.wikipedia.org/wiki/Helsinki

    Open URL (y/n)?



