******
korona
******

|travis| |coveralls|

Korona helps you to generate HTML pages from the given inputs(HTML Tags and Attributes) without writing the HTML code.

Links
=====

- Project: https://github.com/bharadwajyarlagadda/korona
- Documentation: http://korona.readthedocs.io
- TravisCI: https://travis-ci.org/bharadwajyarlagadda/korona

Features
========

- Supported on Python 2.7 and Python 3.3+
- With this package, you can avoid writing direct HTML code.


.. |travis| image:: https://img.shields.io/travis/bharadwajyarlagadda/korona/master.svg?style=flat-square
    :target: https://travis-ci.org/bharadwajyarlagadda/korona

.. |coveralls| image:: https://img.shields.io/coveralls/bharadwajyarlagadda/korona/master.svg?style=flat-square
    :target: https://coveralls.io/r/bharadwajyarlagadda/korona


Changelog
=========


v0.1.0
------

- First release.
- Added classes for building some of the tags:

  - <a></a>
  - <abbr></abbr>
  - <acronym></acronym>
  - <address></address>
  - <area>
  - <article></article>
  - <b></b>
  - <base>
  - <button></button>
  - <canvas></canvas>
  - <caption></caption>
  - <cite></cite>

Caveats:

- Korona has no ability to construct inner tags. (For ex. <address><p>Hi There</p></address>)
- Korona will be added with constructing the inner tags in the next release.


