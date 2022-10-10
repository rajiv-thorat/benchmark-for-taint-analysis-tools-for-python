#!/bin/sh

if [ -d '/code' ]; then
    pip install -r /code/requirements.txt
fi

time -o /op/non_exec_metrics.txt pyre analyze --no-verify --save-results-to /op