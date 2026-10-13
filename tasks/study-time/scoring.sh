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

check test_prints_totals "Program prints the total time for each subject"
check test_sums_same_subject "Sessions of the same subject are summed"
check test_separate_subjects "Different subjects are kept separate"
check test_single_session "A single session is handled"
check test_empty_sessions "An empty session list gives an empty result"
check test_accented_subject_and_zero_minutes "Accented subjects and zero minutes are handled"

to_json "$score" "${results[@]}"
