
# Overview

Basic CLI application to keep track of tasks\
Tasks are accessible in the `tasks.json` file in the same directory as project\
Each task has the following properties:

- ID
- Description / Task name
- Status
- Creation date
- Uptade date

# How to Use

### Windows

1. Install Python https://www.python.org
2. Set the Command Prompt current working directory as the file directory
3. Enter the file name with `.py` suffix
4. Enter one of the given commands with proper arguments (separate each argument with a space)

# Commands

- add (task name) **[string]**
- delete (task ID to delete) **[int]**
- update (task ID to update and new task description) **[int]** **[string]**
- mark_done (task ID) **[int]**
- mark_in_progress (task ID) **[int]**
- list_all_tasks (no arguments)
- list_to_do (no arguments)
- list_done (no arguments)
- list_in_progress (no arguments)

### Example prompt

`main.py add Task name`\
`main.py mark_done 2`\
`main.py list_all_tasks`

# Credits

Idea: https://github.com/kamranahmedse \
Code : https://github.com/piotr-czarnecki-dev