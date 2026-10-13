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

check test_prints_results_and_status "Program prints the results and the book statuses"
check test_borrow_free_book "A free book can be borrowed"
check test_borrow_taken_book "A borrowed book cannot be borrowed again"
check test_borrow_unknown_book "An unknown book cannot be borrowed"
check test_return_borrowed_book "A borrowed book can be returned"
check test_return_invalid_book "A free or unknown book cannot be returned"

to_json "$score" "${results[@]}"
