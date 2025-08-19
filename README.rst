Prezentprogramo
===============
Prezentprogramo is a tool to make impress.js_ presentations from
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
Simple but not the best way to install

.. code:: sh

    pip3 install prezentprogramo

It is better to follow the following steps instead because 
there will be less problems in the long run.

Prepare Environment
^^^^^^^^^^^^^^^^^^^
These steps can be done once. You don't need to repeat them unless you really need to.

`uv <https://github.com/astral-sh/uv>`_ is a Python package and project manager.
Using uv has multiple benefits including installing any version of python3 and
related packages on it. uv can reduce many conflicts and problems you may face if you use pip alone.
While it is not necessary but I would recommend to use it instead of pip.

#. Install the latest python3 
    #. uv 

        .. code:: sh
        
            # First install curl from
            # https://curl.se/download.html
            # Instead on any debian based linux use the following command
            # apt install curl

            curl -LsSf https://astral.sh/uv/install.sh | sh
            
            # update uv periodically
            
            uv self update
            
      #. Install python3
      
          .. code:: sh
          
              uv python install 3.13.6

#. It is better to use virtual environment in python3
    #. Create virtual environment

        #. Using uv
        
            .. code:: sh
            
                uv venv --python 3.13.6 myvenv 
    
        #. Pure python
        
            .. code:: sh

                python -m venv myvenv
                            
    #. Activate virtual environment whenever you want to use prezentprogramo
    
        .. code:: sh

            source myvenv/bin/activate

Install Prezentprogramo
^^^^^^^^^^^^^^^^^^^^^^^
#. Use the latest changes in github repository

    #. Download `Prezentprogramo <https://github.com/yoosofan/prezentprogramo>`_ repository to a directory, like :code:`~/path/prezentprogramo`
    #. Install Prezentprogramo by
    
        #. uv
          
            .. code:: sh
            
                uv tool install ~/path/prezentprogramo/

        #. Or pip
        
            .. code:: sh

                pip install ~/path/prezentprogramo/

#. Or use pypi.org

    #. uv
        
        .. code:: sh
        
            uv tool install prezentprogramo
            
    #. Or pip
    
        .. code:: sh
        
            pip3 install prezentprogramo
            

Prezentprogramo requires Python 3 and can be installed like any Python package.

It is better to use virtual environment::

    $ cd ~/virtual_environment/path/
    $ python -m venv myvenv
    $ source myvenv/bin/activate

The easiest way to install prezentprogramo is by using pip_ and git, then run::

    $ pip3 install git+https://github.com/yoosofan/prezentprogramo
    
Or download the code in a directory let's name it `~/path/prezentprogramo/` then::
    
    $ pip3 install ~/path/prezentprogramo/
    
    or
    
    $ python3 -m pip install ~/path/prezentprogramo/


Use prezentprogramo::

    $ prezentprogramo prezentprogramo/docs/examples/tutorial.rst

It will automatically open browser if it is possible.
If the browser did not open then run your browser
and type the following link in your browser

Prezentprogramo create a folder by the name of the specified rst file. 
Therefore, using the same name for folders and rst file creates conflicts.

Then you can deactivate virtual environment::

    $ deactivate

Juan Bondi has made videos of how to install Hovercraft:

* Installation on Ubuntu and Debian based computers: https://www.youtube.com/watch?v=tHSJLF9OnKQ
* Installation on Windows: https://www.youtube.com/watch?v=I63I8Az24d8

Chromium-chromedriver is needed to generate PDF from RST presentations files (You can only Install Chrome Browser)

Hovercraft is untested on Windows, but there is no reason it shouldn't work, at least in theory.

TODO
----
* Copy MathJax fonts prezentprogramo/hovercraft/templates/default/js/MathJax/es5/output/chtml/fonts/woff-v2
* Remove extra files:
    * Prevent making extra grap_ii.png for changing yographviz
        * G.draw("test.svg", prog= 'dot', format='svg:cairo') 
        * https://stackoverflow.com/a/72152677/886607
        * https://github.com/liuyug/python-docutils-graphviz/tree/master
        * https://github.com/liuyug/python-docutils-graphviz/blob/master/docutils_graphviz.py
        * https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Adding_vector_graphics_to_the_Web
        * https://docutils-ext.readthedocs.io/en/latest/svgt.html
* Add an option to run a new instance of web browser
* Replace `pyhtml2pdf` by `selenium` because of the following vulnerability:
    * https://security.snyk.io/vuln/SNYK-PYTHON-PYHTML2PDF-6254644
    * https://vuldb.com/?id.254137
    * https://vulners.com/github/GHSA-P3RV-QJ56-2FQX
    * https://www.cvedetails.com/cve/CVE-2024-1647/
    * https://cert.ir/node/6248
    * https://nvd.nist.gov/vuln/detail/CVE-2024-1647
    
    * https://github.com/xhtml2pdf/xhtml2pdf
    * https://github.com/CourtBouillon/weasyprint-samples/tree/master
    * https://github.com/Kozea/WeasyPrint/tree/main
    
    
    * https://github.com/plotly/plotly.py
    * https://plotly.com/python/static-image-export/
    * https://plotly.com/python/bar-charts/
    
    * return [nodes.raw('', parsed, format='html')]   # https://snyk.io/advisor/python/docutils/functions/docutils.parsers.rst.directives.register_directive
    * https://github.com/renatopp/pyramid-blog/blob/7dba5a948af8a61e00fea303367be12e5de6f788/blog/blog/libs/rest/reSTpygments.py#L73
    * https://github.com/renatopp/pyramid-blog/tree/master/blog/blog/libs/rest
    * https://github.com/renatopp/pyramid-blog/blob/master/blog/blog/libs/rest/reSTpygments.py
    * https://github.com/renatopp/pyramid-blog/blob/4cc950d6a82eeaa912c9e1111fe25a8cb836d660/blog/blog/libs/rest/reSTpygments.py#L73

    * https://pygraphviz.github.io/documentation/stable/install.html
* Remove MathJax and use current default as --output-math=MathML

.. _impress.js: http://github.com/bartaz/impress.js
.. _demo: https://regebro.github.io/hovercraft
.. _readthedocs.org: https://hovercraft.readthedocs.io/
.. _pip: http://www.pip-installer.org/en/latest/
