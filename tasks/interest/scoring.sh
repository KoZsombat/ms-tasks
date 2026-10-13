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

check test_asks_for_three_values "Program asks for principal, rate and time"
check test_calculates_interest "Program calculates the simple interest"
check test_fractional_interest "Fractional interest is calculated correctly"
check test_zero_time "Zero time gives zero interest"
check test_zero_rate "Zero rate gives zero interest"
check test_large_numbers "Large numbers are handled"

to_json "$score" "${results[@]}"
