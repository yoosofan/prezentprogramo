pip3 uninstall bildumilo -y

rsync -av --delete ~/research/projects/bildumilo/ ~/temp/bildumilo/

pip3 install ~/temp/bildumilo/

cd ~/research/projects/slide/cm/

#rm -rf rd/

bildumilo rd.rst 
