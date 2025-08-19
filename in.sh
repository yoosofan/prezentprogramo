function run(){
    rsync -av --delete ~/research/projects/prezentprogramo/ ~/temp/prezent/
    uv tool uninstall prezentprogramo
    uv cache clean prezentprogramo
    uv tool install ~/temp/prezent/
    cd ~/research/projects/slide/os/
    prezentprogramo vm.rst 
}  
# ------------

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

# github pypi token to publish
# https://github.com/pypa/gh-action-pypi-publish
# https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

# https://packaging.python.org/en/latest/overview/
#https://packaging.python.org/en/latest/tutorials/packaging-projects/

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

run()