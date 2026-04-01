Prezentprogramo
===============
Prezentprogramo is a tool to make `impress.js <https://github.com/impress/impress.js>`_ presentations from
reStructuredText. For a quick explanation, see one of my `slides <https://yoosofan.github.io/slide/os/ps>`_ or check list of them https://yoosofan.github.io/slide/

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

Full documentation of Hovercraft is available at https://hovercraft.readthedocs.io/en/latest/ , and also in the
documentation subdirectory.

Installation
------------
Simple but not the best way to install

.. code:: sh

    pip3 install prezentprogramo

uv
^^
`uv <https://github.com/astral-sh/uv>`_ is a Python package and project manager.
Using uv has multiple benefits including installing any version of python3 and
related packages on it. uv can reduce many conflicts and problems you may face if you use pip alone.
While it is not necessary but I would recommend to use it instead of pip.
At first, install `curl <https://curl.se/download.html>`_

.. code:: sh

    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv python install 3.14
    uv venv --python 3.14 myvenv
    source myvenv/bin/activate
    uv tool install prezentprogramo

Usage
-----
.. code:: sh

    cd prezentprogramo/docs/examples/
    prezentprogramo cpu.rst

It will automatically open browser if it is possible.
If the browser did not open then run your browser
and type the following link in your browser.

.. code:: sh

    http://127.0.0.1:8000

Prezentprogramo creates a directory by the name of slide if it is possible.
However, it is possible to create a seperate directory too.
For Example you can use my `computer courses slide <https://github.com/yoosofan/slide>`_
to test it

.. code:: sh

  cd projects/slide/os
  prezentprogramo cpu.rst cpu_htmls/

Convert to pdf
-----------------
Install google-chrome

.. code:: sh

  prezentprogramo cpu.rst --pdf cpu.pdf

Or you can take screen shots of pages

Screen Shot
^^^^^^^^^^^^^^^
#. Run prezentprogramo

    .. code:: sh

        prezentprogramo cpu.rst

#. Take screen shot
    * Operating system
        1. for `ubuntu-mate <https://ubuntu-mate.org/download/>`_ <use short cut < Shift + PrtSc >
        2. Select the area
        3. Save
    * Or use `browser screenshot <https://dev.to/n_demia/enhancing-bug-reports-how-to-capture-full-page-screenshots-in-different-browsers-4lbl>`_
#. convert images to pdf
    #. Install tools lilke image magic

          * for debian or ubuntu (especially `ubuntu-mate <https://ubuntu-mate.org/download/>`_ !)

              .. code:: sh

                  sudo apt install imagemagick --fix-missing

          * link https://help.ubuntu.com/community/ImageMagick

    #. convert `*.png` cpu.pdf

        .. code:: sh

            convert *.png cpu.pdf

Or use `dectype <docs/dectype4pdf.rst>`_
