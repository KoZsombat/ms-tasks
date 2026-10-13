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
check test_prints_ten_lines "Program prints exactly ten lines"
check test_table_of_five "Multiplication table of 5 is correct"
check test_table_of_other_number "Multiplication table of another number is correct"
check test_table_of_zero "Multiplication table of 0 is correct"
check test_negative_and_large_numbers "Negative and large numbers are handled"

to_json "$score" "${results[@]}"
