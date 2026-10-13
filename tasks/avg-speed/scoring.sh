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

check test_asks_for_distance_and_time "Program asks for distance and time"
check test_calculates_speed "Program calculates the average speed"
check test_fractional_speed "Fractional speeds are calculated correctly"
check test_one_hour "One hour of travel gives the distance as speed"
check test_zero_distance "Zero distance is handled"
check test_large_numbers "Large numbers are handled"

to_json "$score" "${results[@]}"
