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

check test_asks_for_three_sides "Program asks for three sides"
check test_valid_triangle "Valid triangles are recognized"
check test_one_side_too_long "A too long side makes the triangle invalid"
check test_degenerate_triangle "Sides where two add up to the third are invalid"
check test_side_order_does_not_matter "The order of the sides does not matter"
check test_zero_side "A zero side makes the triangle invalid"

to_json "$score" "${results[@]}"
