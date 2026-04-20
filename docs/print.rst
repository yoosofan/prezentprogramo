It is better to install Google-chrome for converting to pdf.

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

Or use `dectype <dectype4pdf.rst>`_
