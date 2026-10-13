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

check test_asks_for_name "Program asks for the name to search for"
check test_finds_contact "An existing contact is found"
check test_finds_other_contact "Another existing contact is found"
check test_finds_accented_contact "A contact with an accented name is found"
check test_unknown_contact "Unknown, empty and differently cased names are not found"
check test_find_contact_function "find_contact returns the number or None"

to_json "$score" "${results[@]}"
