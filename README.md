# task-tracker

CLI application to keep track of tasks.  
Tasks are accessible in `tasks.json` file in the root directory.  
Each task has the following properties:
- ID
- Description
- Completion status
- Creation date
- Update date

## Table of Contents
- [How to Use](#how-to-use)
- [Commands](#commands)
- [Licence](#license)
- [Credits](#credits)

## How to Use

1. Ensure Python 3.10+ is installed.
2. Open the Terminal in the directory containing `main.py`.
3. Type `main.py` followed by one of the available commands.

## Commands

- `add` (enter task name)
- `delete` (enter task ID to delete)
- `update` (enter task ID to update and new task description)
- `mark_done` (enter task ID)
- `mark_in_progress` (enter task ID)
- `list_all_tasks` (no arguments)
- `list_to_do` (no arguments)
- `list_done` (no arguments)
- `list_in_progress` (no arguments)

### Example Prompt

```bash
main.py add task_name
main.py mark_done 2
main.py list_all_tasks
```

## License

This project is licensed under the MIT License
See [LICENSE](./LICENSE) for more information

## Credits

Idea: https://github.com/kamranahmedse
