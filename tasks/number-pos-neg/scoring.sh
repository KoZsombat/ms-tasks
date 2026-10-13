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

check test_asks_for_number "Program asks for a number"
check test_positive_number "Positive number is recognized"
check test_negative_number "Negative number is recognized"
check test_zero "Zero is recognized"
check test_boundary_values "Numbers next to zero are classified correctly"
check test_large_numbers "Large numbers are classified correctly"

to_json "$score" "${results[@]}"
