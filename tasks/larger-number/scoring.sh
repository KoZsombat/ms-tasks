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

check test_first_is_larger "Returns the first number when it is larger"
check test_second_is_larger "Returns the second number when it is larger"
check test_equal_numbers "Equal numbers are handled"
check test_negative_numbers "Negative numbers are compared correctly"
check test_float_numbers "Decimal numbers are compared correctly"
check test_prints_example_result "Program prints the larger of 3 and 2"

to_json "$score" "${results[@]}"
