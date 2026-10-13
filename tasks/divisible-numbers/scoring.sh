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

check test_asks_for_divisor "Program asks for the divisor"
check test_multiples_of_seven "Multiples of 7 are printed correctly"
check test_multiples_of_ten "Multiples of 10 are printed correctly"
check test_divisor_one_prints_everything "Divisor 1 prints all numbers"
check test_hundred_is_included "100 is included"
check test_divisor_above_hundred_prints_nothing "Divisor above 100 prints nothing"

to_json "$score" "${results[@]}"
