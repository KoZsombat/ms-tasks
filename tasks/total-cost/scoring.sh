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

check test_asks_for_three_prices "Program asks for three prices"
check test_calculates_total "Program calculates the total"
check test_different_prices "Different prices give the correct total"
check test_zero_prices "Zero prices are handled"
check test_equal_prices "Equal prices give the correct total"
check test_large_prices "Large prices are handled"

to_json "$score" "${results[@]}"
