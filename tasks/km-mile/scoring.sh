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

check test_km_to_mile "km_mile() converts kilometers to miles"
check test_mile_to_km "mile_km() converts miles to kilometers"
check test_zero_distance "Zero distance converts to zero"
check test_decimal_distance "Decimal distances are converted correctly"
check test_prints_results "Program prints both example conversions"
check test_no_input "Program does not ask for input"

to_json "$score" "${results[@]}"
