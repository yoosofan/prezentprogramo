Prezenta Aplikaĵo
=================
*The merge of convenience and cool!*

Prezenta is a tool to make impress.js_ presentations from
reStructuredText. For a quick explanation, see the demo_.

Based on `Hovercraft! <https://github.com/regebro/hovercraft>`_

Features
--------
* Write your presentations in a text markup language. No slow, limiting GUI, no annoying HTML!

* Pan, rotate and zoom in 3D, with automatic repositioning of slides!

* A presenter console with notes and slide previews!

* Support for showing mathematical formulas.

* Styling is easy with CSS.

* The slide show generated is in HTML, so you only need a web browser to show it.

* Easy sharing, as it can be put up on a website for anyone to see!

Full documentation of Hovercraft is available at readthedocs.org_, and also in the
documentation subdirectory.

Installation
------------
Prezenta requires Python 3 and can be installed like any Python package.

It is better to use virtual environment::

    $ cd /destination/directory/
    $ python -m venv myvenv
    $ source myvenv/bin/activate

Download the code in a directory let's name it `src_dir/path/`
The easiest way is to install pip_, and then run::

    $ python3 -m pip install /home/ahmad/research/projects/prezenta/

Use prezenta

Then you can deactivate virtual environment::

    $ deactivate

Juan Bondi has made videos of how to install:

* Installation on Ubuntu and Debian based computers: https://www.youtube.com/watch?v=tHSJLF9OnKQ

* Installation on Windows: https://www.youtube.com/watch?v=I63I8Az24d8

Chromium-chromedriver is needed to generate PDF from RST presentations files (You can only Install Chrome Browser)

Hovercraft is untested on Windows, but there is no reason it shouldn't work, at least in theory.


.. _impress.js: http://github.com/bartaz/impress.js
.. _demo: https://regebro.github.io/hovercraft
.. _readthedocs.org: https://hovercraft.readthedocs.io/
.. _pip: http://www.pip-installer.org/en/latest/
