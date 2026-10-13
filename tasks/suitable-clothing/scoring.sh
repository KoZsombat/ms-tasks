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

check test_asks_for_temperature "Program asks for the temperature"
check test_cold_weather "Cold weather suggests a coat"
check test_mild_weather "Mild weather suggests a sweater"
check test_warm_weather "Warm weather suggests a t-shirt"
check test_boundary_ten "Boundary at 10 degrees is correct"
check test_boundary_twenty "Boundary at 20 degrees is correct"

to_json "$score" "${results[@]}"
