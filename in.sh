function old11(){
  
    pip3 uninstall prezentprogramo -y

    rsync -av --delete ~/research/projects/prezentprogramo/ ~/temp/prezentprogramo/

    pip3 install ~/temp/prezentprogramo/

    cd ~/research/projects/slide/cm/

    #rm -rf rd/

    prezentprogramo rd.rst 
}
# ------------

function install_uv_python(){

    # install uv
    # On macOS and Linux.
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv self update
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
    flake8 --ignore=E501 .
    
    uv tool install autopep8
    autopep8 --in-place --aggressive  --recursive --list-fixes --max-line-length 79 .

    uv tool install ini2toml[full]
    ini2toml --help
    ini2toml -o setup.toml setup.cfg

}


rsync -av --delete ~/research/projects/prezentprogramo/ ~/temp/prezent/
uv tool uninstall prezentprogramo
uv cache clean prezentprogramo
uv tool install ~/temp/prezent/
cd ~/research/projects/slide/os/
prezentprogramo vm.rst 
