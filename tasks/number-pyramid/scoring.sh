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

check test_asks_for_rows "Program asks for the number of rows"
check test_prints_requested_number_of_lines "Program prints the requested number of lines"
check test_pyramid_of_five "Pyramid of 5 rows is correct"
check test_pyramid_of_one "Pyramid of 1 row is correct"
check test_pyramid_with_two_digit_numbers "Pyramid with two-digit numbers is correct"
check test_zero_rows_prints_nothing "Zero rows prints nothing"

to_json "$score" "${results[@]}"
