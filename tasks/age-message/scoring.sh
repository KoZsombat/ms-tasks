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

check test_asks_for_age "Program asks for the age"
check test_minor_message "Under 18 gets the minor message"
check test_adult_message "Adults get the adult message"
check test_retired_message "Over 65 gets the retired message"
check test_age_18_is_adult "Age 18 counts as adult"
check test_age_65_is_retired "Age 65 counts as retired"

to_json "$score" "${results[@]}"
