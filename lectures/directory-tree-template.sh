#!/usr/bin/bash
projectName=project
author='Christian Vollmann'
title='Das relaxierte Richardson Verfahren'
date=2022
# CODE
echo $projectName
mkdir $projectName
mkdir $projectName/code
mkdir $projectName/code/docs
mkdir $projectName/code/src
mkdir $projectName/code/examples
mkdir $projectName/code/output
touch $projectName/code/main.py
touch $projectName/code/README.md
touch $projectName/code/src/linalg.py
touch $projectName/code/.gitignore
touch $projectName/code/LICENSE
touch $projectName/code/.pre-commit-config.yaml 
touch 
# TEXT:
mkdir $projectName/text
mkdir $projectName/text/src
mkdir $projectName/text/src/macros
mkdir $projectName/text/src/content
mkdir $projectName/text/media
mkdir $projectName/text/literature
mkdir $projectName/text/literature/pdfs
touch $projectName/text/main.tex
touch $projectName/text/src/macros/commands.tex
touch $projectName/text/src/macros/usepackages.tex
touch $projectName/text/src/macros/style.tex
echo "\author{$author}\title{$title}\date{$date}" > $projectName/text/src/macros/meta.tex
echo "------------------------------------------------------------------"
echo "The following tree has been created:"
tree -L 4 $projectName
