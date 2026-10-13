---
name: finish
description: Create or finish an ms-tasks task. Given just a short task description (no folder name needed), invent a folder name like the existing ones, create tasks/<name>/ with source/main.py if it is missing, then generate scoring.sh, source/test/test.py and source/README.md, following the repo's task conventions and the already finished tasks. Use when creating, finishing, grading or writing tests for a task under tasks/.
argument-hint: <short task description, or an existing task folder>
---

Task: $ARGUMENTS

Short Python programming exercises for Hungarian-speaking beginners. Each task lives in its own folder under `tasks/` and is auto-graded in a sandbox.

## Task layout

Reference example: `tasks/greeting-task/`.

```
tasks/<name>/
├── scoring.sh          # grader, runs in the sandbox
└── source/             # copied to /home/oracle/project in the sandbox
    ├── README.md       # task description for the student (Hungarian)
    ├── main.py         # reference solution
    └── test/
        └── test.py     # unittest tests that scoring.sh runs
```

- `source/main.py` is the reference solution. Tests must pass against it.
- Student-facing text (README, prompts in `main.py`) is in Hungarian. Code identifiers, test names and `scoring.sh` result messages are in English.

## `test.py` conventions

- `unittest` and the standard library only. No pytest, no third-party packages.
- 2-space indentation, like the example.
- Run `main.py` by importing it fresh on every call: `sys.modules.pop('main', None)` then `importlib.import_module('main')`. Patch `builtins.input` (`return_value`, or `side_effect` for several inputs) and capture stdout with `contextlib.redirect_stdout`. Put this in a `run_main(...)` helper.
- One behavior per test method, named `test_<behavior>`. Each method name must be unique across the file, because `scoring.sh` selects tests with `-k <name>` and expects exactly one match.
- Test behavior, not exact wording: check that values appear in the output, that `input` was called the expected number of times, that edge cases (accented characters like `Árvíztűrő`, empty input, etc.) don't crash. Don't assert on the exact prompt or greeting text unless the README requires it.
- End the file with `if __name__ == '__main__': unittest.main()` and the run command as a comment:
  `# python3 -m unittest discover -s test -p "test.py" -v`

## `README.md` conventions

Copy the structure and tone of `tasks/greeting-task/source/README.md`. Write it in Hungarian for complete beginners, and spell out every step:

- `# <Cím>`: a short Hungarian title.
- `## Feladat`: one or two sentences on what the program does.
- `## Követelmények`: a numbered list with one concrete step per item, in the order the student writes the code. Under each step that uses a new construct (`input`, `print` with an f-string, `def`, `if`/`else`, `return`, function calls, etc.), add a short labelled snippet (`Beolvasás:`, `Kiírás:`, `Függvény:`, `Feltétel:`…) in a ```` ```py ```` block. Use generic placeholders like `változó` or `szöveg`, not the finished solution. Name any identifier the tests depend on (function names, parameter order), and give one concrete example of input and output.
- After the list, one line on which edge cases must also work (the ones the tests cover).
- `## Értékelés`: "A megoldást N teszt ellenőrzi (1-1 pont):", then one Hungarian bullet per test in `scoring.sh` order. If the tests don't check exact wording, say so at the end.
- `## Futtatás` with `python3 main.py`, and `## Teszt` with `python3 -m unittest discover -s test -p "test.py" -v`, both in plain ```` ``` ```` blocks.

The README must describe what `main.py` actually does. Don't add requirements that the reference solution doesn't meet.

## `scoring.sh` conventions

Copy the structure of `tasks/greeting-task/scoring.sh` exactly:

- `source /protected/utils.sh`, `cd /home/oracle/project` with the `to_json 0 "+0 Project directory not found"` fallback.
- The `check()` function runs `python3 -m unittest discover -s test -p "test.py" -k "$1"` and requires both exit code 0 and `Ran 1 test` in the output.
- One `check <test_method_name> "<English description>"` line per test method in `test.py`, in the same order, 1 point each.
- Finish with `to_json "$score" "${results[@]}"`.
- LF line endings and a `#!/bin/bash` shebang. The file must stay executable.

## Procedure

Creates a whole task (if needed) and its grading files.

Input: `$ARGUMENTS`, normally just a short description of the task in any language (e.g. `calculate simple interest`, `szorzótábla 1-től 10-ig`). The user does not give a folder name. It can also be the name of an existing folder under `tasks/` (e.g. `leap-year`), to finish that task.

Steps:
0. Resolve the task folder:
   - List `tasks/`. If the argument is (or is an obvious typo of) an existing folder name, use that folder. If the folder name is misspelled, tell the user and rename it only if they typed the correct spelling.
   - If the description matches an existing task that has no `scoring.sh` yet, use that folder.
   - Otherwise it is a new task: invent the folder name yourself, then create `tasks/<name>/source/`. The name follows the existing ones: 2–3 lowercase English words joined by hyphens, describing what the program does (`total-cost`, `leap-year`, `valid-triangle`, `avg-speed`, `number-pos-neg`, `temp-trends`). It must not collide with an existing folder. Don't ask the user to pick a name; mention the chosen name in the final report.
   - Look at 3–4 finished tasks (folders that have `scoring.sh`, e.g. `greeting-task`, `suitable-clothing`, `temp-trends`, `library`) and use them as examples for the style of `main.py`, `test.py`, `README.md` and `scoring.sh`. Prefer ones similar to the new task (input/arithmetic, if/else, loops, functions, lists/dicts).
1. If `source/main.py` is missing or empty, write it as the reference solution. Keep it short and beginner-level, like the existing ones:
   - Hungarian prompts and output text; English identifiers; 2-space indentation.
   - Simple constructs only: `int(input("..."))`, `if`/`elif`/`else`, `for`/`while`, `def` + `return`, lists/dicts, f-string `print`. No classes, no imports unless needed.
   - Input-driven programs use `input`; function/list/dict tasks use a hardcoded data structure plus functions and print the results, so tests can import and call them.
   - It must be correct, including edge cases the task description implies (e.g. the full leap-year rule). If the description is ambiguous, choose the simplest sensible reading and state the assumption in the final report.
   Then continue. Don't ask for confirmation first unless the task is too vague to guess.
2. Read `source/main.py` and `source/README.md` if it exists, to work out what the program must do. Run `main.py` once with sample input to check it works. If an existing `main.py` has a bug (wrong result, crash on normal input), stop and report it instead of writing tests that encode the bug. Fix `main.py` only when the user asked for it or when you wrote it in this run.
3. Write `source/test/test.py`: 3–6 tests covering the main requirements plus edge cases, following the conventions above.
4. Write `scoring.sh` with one `check` line per test. Make it executable (`chmod +x`).
5. If `source/README.md` exists, update its `## Értékelés` section to list the tests (one Hungarian bullet each, test count and points matching). If there is no README, write one following the README conventions above.
6. Run the tests against the reference solution from the `source` folder: `python3 -B -m unittest discover -s test -p "test.py" -v`. Every test must pass. Also run each `-k <name>` and confirm it reports `Ran 1 test`. Always pass `-B` so no `__pycache__` folders are created, and delete any that appear anyway.
7. Report, in Hungarian if the user wrote Hungarian: which files were created (and whether `main.py` was written by you), which tests were created and what each one checks, and any assumption or problem found in `main.py`.

Don't modify an existing, user-written `main.py` unless asked. If it seems to contradict the README, stop and ask.
