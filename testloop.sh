#!/bin/bash

source .venv/bin/activate

while true; do
    clear
    if [ "$1" == "verbose" ]
    then
      pytest -x -vv kata
    else
      pytest kata
    fi

    fswatch **/*.py -1
done
