Rewrite to use docutils directly
---------------------------------
MyST-Parser
^^^^^^^^^^^
https://github.com/executablebooks/MyST-Parser
https://myst-parser.readthedocs.io/en/latest/


docutils
^^^^^^^^
docutils change directive options
https://www.docutils.org/docs/howto/rst-directives.html
https://www.docutils.org/docs/howto/rst-roles.html
https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections

docutils add options to current directive
https://docutils.sourceforge.io/docs/user/config.html
https://www.docutils.org/docs/user/config.html#configuration-file-sections-entries
https://stackoverflow.com/questions/32167384/how-do-i-convert-a-docutils-document-tree-into-an-html-string/32168938#32168938
https://stackoverflow.com/questions/75164714/how-to-create-a-new-document-in-sphinx-docutils-by-api

https://github.com/regebro/hovercraft/commit/7f714b5592749f9846fa2a115915168586da309a
https://github.com/regebro/hovercraft/commit/a4d470a2562a38e1cc14f8561bb1c1c9f0bfaa0c
https://github.com/regebro/hovercraft/commit/aa3d2fb593106b858b84fb2ba43792fa967f9d69
https://github.com/regebro/hovercraft/commit/3ee4a44a7d1708ba6bb89f9d54371bcf68c98c56
https://github.com/regebro/hovercraft/commit/2ede7bff05a127fef8ab06a87cc3a86f94ac25ee
https://github.com/regebro/hovercraft/commits/master/?after=251890b328bb26540b37498c21647beeaa69a7c9+314

https://github.com/jwodder/rst2json/blob/master/src/rst2json/writers/html5.py

https://stackoverflow.com/questions/47337009/rst2html-on-full-python-project


https://rst2html5.readthedocs.io/en/latest/_modules/docutils/nodes.html

https://rst2html5.readthedocs.io/_/downloads/en/stable/pdf/

https://docutils.sourceforge.io/docs/user/rst/quickref.html#example-callout
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html


Publish project
^^^^^^^^^^^^^^^
github pypi token to publish
https://github.com/pypa/gh-action-pypi-publish
https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

https://packaging.python.org/en/latest/overview/
https://packaging.python.org/en/latest/tutorials/packaging-projects/

https://discuss.python.org/t/how-to-release-python-code-on-github/38559
https://realpython.com/pypi-publish-python-package/
https://realpython.com/github-actions-python/
https://anshumanfauzdar.medium.com/using-github-actions-to-bundle-python-application-into-a-single-package-and-automatic-release-834bd42e0670
https://docs.github.com/en/actions/tutorials/build-and-test-code/python
https://stackoverflow.com/questions/77385800/how-do-i-make-a-github-project-automatically-install-my-python-packages-when-dow
github python applicatin create build files automatically
https://github.com/actions/toolkit
https://github.com/actions/toolkit/blob/main/.github/workflows/unit-tests.yml

test pytest
https://docs.pytest.org/en/stable/
github/workflows/test.yml pip install -e ".[test]"
https://github.com/regebro/hovercraft/tree/master/.github/workflows

https://pypi.org/project/Prezentprogramo/

Python syntax checkers break lines
https://discuss.python.org/t/pep-7-break-lines-before-operators-like-pep-8/62402/4
https://stackoverflow.com/questions/7942586/correct-style-for-line-breaks-when-chaining-methods-in-python/7942617#7942617
https://inventwithpython.com/blog/comparing-python-linters-2022.html
https://trunk.io/learn/comparing-ruff-flake8-and-pylint-linting-speed
https://pythonspeed.com/articles/pylint-flake8-ruff/

PDF
----
https://github.com/rggarcia/impressjs2pdf
https://github.com/impress/impress.js/tree/master/src/plugins/mobile

rst2html5
^^^^^^^^^^
After changing the whole structure to directly use rst2html5,
then it could be easier to make a suitable html for print.

opera webdriver
^^^^^^^^^^^^^^^
https://github.com/operasoftware/operachromiumdriver
https://stackoverflow.com/questions/24719270/selenium-webdriver-and-opera-driver
https://github.com/operasoftware/operachromiumdriver/blob/master/examples/desktop_selenium_4.x.py

deck2pdf-python
^^^^^^^^^^^^^^^
https://github.com/astefanutti/decktape

https://github.com/attakei/deck2pdf-python

https://pypi.org/project/deck2pdf/

Python library to generate PDF from presentation html

deck2pdf is converter from your html slide into PDF format keeping slide layout.
Use as CLI only

pipx run deck2pdf https://slides.attakei.net/pyconjp-2022/ output.pdf

uvx deck2pdf https://slides.attakei.net/pyconjp-2022/ output.pdf

.. code::

	uv tool install playwright
	playwright install
	uv tool install deck2pdf

https://stackoverflow.com/questions/73171905/chromium-executable-doesnt-exist-for-running-playwright-within-a-deployed-googl

Mobile Devices
--------------
https://github.com/impress/impress.js/tree/master/src/plugins/mobile

Remote control
--------------
python control impress.js remote server

Impress.js server
^^^^^^^^^^^^^^^^^
https://github.com/tompro/impress-server

Impress-server enables you to share an impress.js presentation with other users. It is not only a remote control, but every user who opens the presentation while it is in presentation mode, will have the state of the presentation synced in real time to his browser.
What problem does it solve ?

In our company we permanently have video conferences with customers. Whenever we want to run a presentation for them we have to do this via a screen sharing tool. Screen sharing is fine but the quality is poor and it uses a lot of bandwith. With impress-server you can run a remote presentation with nearly no bandwidth useage at all and in full impress.js quality.

In addition to that, you can use impress-server just to give you the ability to remote control your presentation with your phone or another computer.
Install

Install via NPM:

npm install -g impress-server

other
^^^^^
https://stackoverflow.com/questions/19626684/how-can-i-make-reveal-js-work-with-a-presenter-remote

impress.js more information
---------------------------
https://github.com/impress/impress.js/blob/master/GettingStarted.md
https://dhananjaypurohit.medium.com/impress-js-a-better-way-of-making-presentations-4e5d7686e98c
http://platika.github.io/impress.js/

Similar projects
----------------
https://github.com/scommab/impressor
http://scommab.github.io/impressor/show/index.html#/step-2

features
---------
disable and enable mouse or keyboard


Other
------
* prepare for readthedocs and add to it.
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

COMMENT11


.. code:: sh

	function install_uv_python(){

		# install uv
		# On macOS and Linux.
		curl -LsSf https://astral.sh/uv/install.sh | sh

		uv self update
		uv tool upgrade --all

		uv python install 3.13.6
		uv venv --python 3.13.6  ~/install/uv13.6

		source ~/install/uv13.6

		uv tool install black
		black . --check
		black .

		uv tool install ruff@latest

		ruff check
		ruff check --fix

		uv tool install flake8
		flake8 .
		flake8 . --ignore=E501,W503,E203

		uv tool install autopep8
		autopep8 --in-place --aggressive  --recursive --list-fixes --max-line-length 79 .

		uv build

		# uv publish dist/*
		# uv publish --token <your_pypi_token>

		twine check --strict dist/*
		twine upload dist/*
	}

	function old11(){

		pip3 uninstall prezentprogramo -y

		rsync -av --delete ~/research/projects/prezentprogramo/ ~/temp/prezentprogramo/

		pip3 install ~/temp/prezentprogramo/

		cd ~/research/projects/slide/cm/

		#rm -rf rd/

		prezentprogramo rd.rst

		uv tool install ini2toml[full]
		ini2toml --help
		ini2toml -o setup.toml setup.cfg

	}

related
-------
uv
^^^^
https://blog.appsignal.com/2025/09/24/switching-from-pip-to-uv-in-python-a-comprehensive-guide.html

date based
----------
2026/04/01
^^^^^^^^^^
* Change created folder name for each rst slide to ``rst_name.htmls.prezaentprogramo/``