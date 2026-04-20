Prezentprogramo
===============
Prezentprogramo is a tool to make `impress.js <https://github.com/impress/impress.js>`_ presentations from
reStructuredText. For a quick explanation, see one of my `slides <https://yoosofan.github.io/slide/os/ps>`_ or check list of them https://yoosofan.github.io/slide/

Based on `Hovercraft! <https://github.com/regebro/hovercraft>`_

Installation
------------
.. code:: sh

    pip3 install prezentprogramo

More on installation on `install <docs/install.rst>`_

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
.. code:: sh

  prezentprogramo cpu.rst --pdf cpu.pdf
