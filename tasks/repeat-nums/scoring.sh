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


check test_asks_for_answer "Program asks for the answer"
check test_shows_numbers "Program shows the numbers to repeat"
check test_correct_answer "Correct answer is praised"
check test_wrong_answer "Wrong answer is reported"
check test_wrong_order "Right numbers in wrong order are reported"
check test_empty_answer "Empty answer is handled"

to_json "$score" "${results[@]}"
