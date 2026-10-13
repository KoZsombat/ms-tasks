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

check test_prints_trend_counts "Program prints the trend counts"
check test_rising_temperatures "Rising temperatures are counted"
check test_falling_temperatures "Falling temperatures are counted"
check test_constant_temperatures "Unchanged temperatures are counted"
check test_mixed_temperatures "Mixed temperatures are counted correctly"
check test_short_lists "Empty and one-element lists are handled"

to_json "$score" "${results[@]}"
