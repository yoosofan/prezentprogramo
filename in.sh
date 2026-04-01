#!/bin/bash
function commot_tasks1(){
    rsync -av --delete ~/research/projects/prezentprogramo/ ~/temp/prezent/

    #uv tool uninstall --all

    uv tool uninstall prezentprogramo
    uv cache clean prezentprogramo

    #uv cache clean

    uv tool install ~/temp/prezent/

}

function run22(){
    commot_tasks1

    cd ~/research/projects/slide/os/
    rm -rf cpu/
    prezentprogramo cpu.rst
}

function bildumilo_test_run(){
    commot_tasks1

    cd ~/temp/prezent/
    bildumilo ~/temp/prezent/tests/test_data/simple.rst ~/temp/prezent/tests/test_data/simple.rst.html
    cd -
}

run22
# source /home/ahmad/install/uv.virtual.environments/p3.14.3/bin/activate
#bildumilo_test_run

: <<'COMMENT11'
uv self update
uv tool upgrade --all

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

# by uv

    uv build

    # uv publish dist/*
    # uv publish --token <your_pypi_token>

uv tool install build
uv tool install wheel

python -m build

twine check --strict dist/*
twine upload dist/*

### Old

uv tool install ini2toml[full]
ini2toml --help
ini2toml -o setup.toml setup.cfg

COMMENT11
