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


check test_add "add returns the sum"
check test_subtract "subtract returns the difference"
check test_multiply "multiply returns the product"
check test_divide_numbers "divide returns the quotient"
check test_divide_by_zero "Division by zero returns 0"
check test_prints_results "Program prints the four results"

to_json "$score" "${results[@]}"
