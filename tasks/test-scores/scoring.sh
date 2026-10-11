#!/bin/bash

source /protected/utils.sh

cd /home/oracle/project || {
    to_json 0 "+0 Project directory not found"
    exit
}

score=0
results=()

check() {
    out=$(python3 -m unittest discover -s test -p "test.py" -k "$1" 2>&1)
    if [ $? -eq 0 ] && [[ "$out" == *"Ran 1 test"* ]]; then
        score=$((score + 1))
        results+=("+1 $2")
    else
        results+=("+0 $2")
    fi
}

check test_prints_average "Program prints the average score"
check test_prints_highest "Program prints the highest score"
check test_prints_passed_count "Program prints the number of passing students"
check test_passed_at_threshold "passed() accepts scores of 40 and above"
check test_failed_below_threshold "passed() rejects scores below 40"
check test_no_input "Program does not ask for input"

to_json "$score" "${results[@]}"
