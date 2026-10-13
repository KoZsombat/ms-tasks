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

check test_asks_for_score "Program asks for the score"
check test_grade_1 "Scores below 40 give grade 1"
check test_grade_2 "Scores from 40 to 59 give grade 2"
check test_grade_3 "Scores from 60 to 79 give grade 3"
check test_grade_4 "Scores from 80 to 89 give grade 4"
check test_grade_5 "Scores from 90 give grade 5"

to_json "$score" "${results[@]}"
