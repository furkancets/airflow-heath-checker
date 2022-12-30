#!/bin/bash

export PYTHON_MAIN="main.py"

source /Users/furkancetukkaya/PycharmProjects/health-checker/airflow-health-cheker/hook-env/bin/activate

cd "/Users/furkancetukkaya/PycharmProjects/health-checker/airflow-health-cheker" && echo $PWD && python3 $PYTHON_MAIN "$@"
