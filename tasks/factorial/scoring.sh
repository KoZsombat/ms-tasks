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

check test_asks_for_number "Program asks for the number"
check test_factorial_of_five "Factorial of 5 is correct"
check test_factorial_of_one "Factorial of 1 is correct"
check test_factorial_of_other_number "Factorial of another number is correct"
check test_factorial_of_large_number "Factorial of a large number is correct"
check test_factorial_of_zero "Factorial of 0 is correct"

to_json "$score" "${results[@]}"
