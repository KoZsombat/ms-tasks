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

check test_asks_until_zero "Program keeps asking for expenses until 0"
check test_several_expenses "Several expenses are summed up"
check test_single_expense "A single expense is counted"
check test_no_expense "No expense is handled"
check test_spent_more_than_earned "Overspending gives a negative balance"
check test_large_numbers "Large numbers are handled"

to_json "$score" "${results[@]}"
