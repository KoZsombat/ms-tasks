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

check test_rectangle_area "rectangle_area() returns the area of a rectangle"
check test_triangle_area "triangle_area() returns the area of a triangle"
check test_triangle_half_result "triangle_area() returns non-integer results correctly"
check test_decimal_sides "Both functions work with decimal numbers"
check test_prints_results "Program prints both example areas"
check test_no_input "Program does not ask for input"

to_json "$score" "${results[@]}"
