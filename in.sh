#!/bin/bash

function run22(){
    rsync -av --delete ~/research/projects/prezentprogramo/ ~/temp/prezent/
    uv tool uninstall prezentprogramo
    uv cache clean prezentprogramo
    uv tool install ~/temp/prezent/
    cd ~/research/projects/slide/os/
    rm -rf cpu/
    prezentprogramo cpu.rst
}

run22

# ------------

: <<'COMMENT11'

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


# github pypi token to publish
# https://github.com/pypa/gh-action-pypi-publish
# https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

# https://packaging.python.org/en/latest/overview/
# https://packaging.python.org/en/latest/tutorials/packaging-projects/

https://discuss.python.org/t/how-to-release-python-code-on-github/38559
# https://realpython.com/pypi-publish-python-package/
# https://realpython.com/github-actions-python/
# https://anshumanfauzdar.medium.com/using-github-actions-to-bundle-python-application-into-a-single-package-and-automatic-release-834bd42e0670
# https://docs.github.com/en/actions/tutorials/build-and-test-code/python
# https://stackoverflow.com/questions/77385800/how-do-i-make-a-github-project-automatically-install-my-python-packages-when-dow
# github python applicatin create build files automatically
# https://github.com/actions/toolkit
# https://github.com/actions/toolkit/blob/main/.github/workflows/unit-tests.yml

# test pytest
# https://docs.pytest.org/en/stable/
# github/workflows/test.yml pip install -e ".[test]"
# https://github.com/regebro/hovercraft/tree/master/.github/workflows

# https://pypi.org/project/Prezentprogramo/

# Python syntax checkers break lines
# https://discuss.python.org/t/pep-7-break-lines-before-operators-like-pep-8/62402/4
# https://stackoverflow.com/questions/7942586/correct-style-for-line-breaks-when-chaining-methods-in-python/7942617#7942617
# https://inventwithpython.com/blog/comparing-python-linters-2022.html
# https://trunk.io/learn/comparing-ruff-flake8-and-pylint-linting-speed
# https://pythonspeed.com/articles/pylint-flake8-ruff/


TODO
----
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
