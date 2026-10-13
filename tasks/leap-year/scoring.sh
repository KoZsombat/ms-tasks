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

check test_asks_for_year "Program asks for the year"
check test_leap_year "Years divisible by 4 are leap years"
check test_common_year "Years not divisible by 4 are not leap years"
check test_century_is_not_leap_year "Centuries not divisible by 400 are not leap years"
check test_divisible_by_400_is_leap_year "Years divisible by 400 are leap years"

to_json "$score" "${results[@]}"
