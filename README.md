# 📝 To Do List (Python CLI)

A simple command-line to-do list manager written in Python. Tasks are saved to a CSV file so your list persists between sessions.

---

## Features

- Add new tasks
- View all current tasks
- Remove tasks by number
- Mark tasks as complete
- Data saved automatically to `todolist.csv` — nothing is lost when you close the program

---

## Install Dependencies

```bash
pip install pandas
```

---

## Usage

Make sure `todolist.csv` and `todolist.py` are in the same folder, then run:

```bash
python todolist.py
```

You'll be prompted to enter a number for each action:

```
1 - Add Task
2 - View Tasks
3 - Remove Task
4 - Mark Task as Complete
5 - Exit
```

### Adding a Task
Enter `1` and type your task. You can keep adding tasks one after another. Type `exit` when you're done.

### Viewing Tasks
Enter `2` to print all current tasks to the terminal.

### Removing a Task
Enter `3` to view the list, then enter the number of the task you want to delete. The list is automatically re-numbered after removal.

### Marking a Task as Complete
Enter `4` to view the list, then enter the number of the task you want to mark done. The task will be updated with `- (Task Completed)` appended to it.

---

## Notes

- The program exits after certain actions. Just re-run `todolist.py` to continue managing your list.
- Do not open `todolist.csv` in Excel, as it may alter the `:` delimiter. Use a plain text editor if needed.
