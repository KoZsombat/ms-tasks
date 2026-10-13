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

check test_correct_first_answer_asks_once "Correct first answer asks only once"
check test_correct_answer_prints_message "Correct answer prints a message"
check test_asks_again_after_wrong_answer "Asks again after a wrong answer"
check test_asks_until_correct_answer "Keeps asking until the answer is correct"
check test_stops_after_correct_answer "Stops asking after the correct answer"
check test_empty_and_accented_answers_are_wrong "Empty and accented answers are handled as wrong"

to_json "$score" "${results[@]}"
