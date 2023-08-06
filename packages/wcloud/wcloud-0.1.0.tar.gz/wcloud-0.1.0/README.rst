===============================
wCloud
===============================

**A command line tool to generate wordclouds.**


.. image:: https://img.shields.io/pypi/v/wcloud.svg
        :target: https://pypi.python.org/pypi/wcloud

.. image:: https://img.shields.io/travis/neocortex/wcloud.svg
        :target: https://travis-ci.org/neocortex/wcloud

.. image:: https://readthedocs.org/projects/wcloud/badge/?version=latest
        :target: https://wcloud.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/neocortex/wcloud/badge.svg?branch=master
        :target: https://coveralls.io/github/neocortex/wcloud?branch=master


**About**

This is a command line wrapper around https://github.com/amueller/word_cloud
using click_.

.. _click: http://www.click.pocoo.org


**Installation**
::

    $ pip install wcloud

**Usage**

Basic::

   $ wcloud input.txt

With options::

    $ wcloud -b white -w 300 -h 200 -o output.png input.txt

With mask::

    $ wcloud -m mask.png -o threepio.png threepio.txt

.. image:: examples/wordcloud.png
   :height: 1849
   :width: 1512
   :scale: 50

* Free software: MIT license
* Documentation: https://wcloud.readthedocs.io.
