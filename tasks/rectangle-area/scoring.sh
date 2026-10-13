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

check test_asks_for_two_values "Program asks for two values"
check test_calculates_area "Program calculates the area"
check test_different_values "Different values give the correct area"
check test_square "Equal sides give the correct area"
check test_zero_side "Zero side is handled"
check test_large_numbers "Large numbers are handled"

to_json "$score" "${results[@]}"
