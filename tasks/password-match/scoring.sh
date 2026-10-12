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


check test_asks_for_password "Program asks for the password"
check test_correct_password "Correct password is accepted"
check test_wrong_password "Wrong password is rejected"
check test_case_sensitive "Password check is case sensitive"
check test_empty_password "Empty password is rejected"
check test_accented_password "Accented password is rejected without crashing"

to_json "$score" "${results[@]}"
