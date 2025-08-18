function old11(){
  
    pip3 uninstall bildumilo -y

    rsync -av --delete ~/research/projects/bildumilo/ ~/temp/bildumilo/

    pip3 install ~/temp/bildumilo/

    cd ~/research/projects/slide/cm/

    #rm -rf rd/

    bildumilo rd.rst 
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


rsync -av --delete ~/research/projects/bildumilo/ ~/temp/bildo/
uv tool uninstall bildumilo
uv cache clean bildumilo
uv tool install ~/temp/bildo/
cd ~/research/projects/slide/os/
bildumilo vm.rst 
