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


check test_list_contents "List contains the numbers 1-5"
check test_prints_one_line "Program prints exactly one line"
check test_prints_position_of_three "Program prints the position of 3"
check test_output_matches_list_index "Output matches the index of 3 in the list"
check test_does_not_ask_for_input "Program does not ask for input"

to_json "$score" "${results[@]}"
