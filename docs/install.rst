
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
    uv tool install docutils --with pygments --force
    uv tool install prezentprogramo

