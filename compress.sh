#!/usr/bin/env bash


ops=('assets/' 'Dockerfile' '.dockerignore' '.gitignore' 'Pipfile' 'Pipfile.lock')

data=('data/' 'output/')

src=('*.ipynb' '*.py')

docs=('README.md' 'CMPS_144_FINAL_PAPER.pdf')

EVERYTHING="${ops[@]} ${data[@]} ${src[@]} ${docs[@]}"
zip -r -u -1 -9 submission/project.zip $EVERYTHING
