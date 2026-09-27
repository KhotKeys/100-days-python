# Day 01: Project Tracker (Command-Line Interface)

A command-line app for keeping track of academic projects. Add projects with their series, academic code and dates, mark them as done, delete them, and pick up where you left off next time.

## Features

- Add a project with name, series, academic code, start date and end date
- View all projects with a done / not done status
- Mark a project as done
- Delete a project, with a confirmation step
- Saves automatically to a local JSON file, so nothing is lost when you quit
- Handles bad input without crashing (empty names, letters instead of numbers, out of range choices, a damaged save file)

## How to run

Requires Python 3.10 or newer. No extra packages needed.

```bash
cd day-01
python3 main.py
```

## Example

```text
=== Project Tracker ===
1. Add a project
2. View projects
3. Mark a project as done
4. Delete a project
5. Quit
Choose an option: 2
1. [x] Assignment - 01 - 01 - 2026-09-27 to 2026-12-27
2. [ ] Capstone - Series 1 - BSE-401 - 2026-09-01 to 2026-12-15
```

## How data is stored

Projects are saved to `projects.json` in this folder after every change. The file is ignored by Git, so personal data stays on your machine. If the file gets damaged, the app keeps a backup as `projects.json.bak` and starts with an empty list.

## What I learned

- Structuring a program into small functions with one job each
- Using a `while True` loop with `break` for an interactive menu
- Storing records as dictionaries instead of joined strings, so fields stay usable
- Validating input with `try` / `except ValueError` and range checks
- Why `if index is None` is safer than `if not index` when index 0 is valid
- How a trailing comma turns a value into a tuple, and the error it causes
- Reading and writing JSON with `json` and `pathlib`, and using `with` to handle files safely

## Ideas for later

- Validate dates with the `datetime` module
- Edit an existing project
- Sort or filter by end date or series
- Show overdue projects
