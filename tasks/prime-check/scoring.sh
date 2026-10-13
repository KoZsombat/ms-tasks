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

check test_asks_for_number "Program asks for the number"
check test_small_primes "Small primes are recognized"
check test_composite_numbers "Composite numbers are not prime"
check test_one_is_not_prime "1 is not prime"
check test_zero_and_negative_are_not_prime "0 and negative numbers are not prime"
check test_large_prime "Large prime is recognized"

to_json "$score" "${results[@]}"
