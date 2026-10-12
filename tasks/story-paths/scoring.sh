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


check test_asks_for_option "Program asks for the story path"
check test_first_path "Option 1 selects the first path"
check test_second_path "Option 2 selects the second path"
check test_invalid_option "Invalid option is reported"
check test_empty_option "Empty input is reported as invalid"
check test_paths_differ "The three outcomes give different outputs"

to_json "$score" "${results[@]}"
