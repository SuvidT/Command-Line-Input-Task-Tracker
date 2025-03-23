# Project Goal
This is a Command Line Interface to track tasks.

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file.

## Features:
- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks (all, done, not done, in progress)

### Constraints:
- Use any programming language
- Use **positional arguments** for user inputs
- Store tasks in a **JSON file** in the current directory
- **Create JSON file if it does not exist**
- Use the **native file system module** for file interactions
- **No external libraries or frameworks**
- Handle **errors and edge cases gracefully**

### Task Properties:
- `id`: Unique task identifier
- `description`: Task description
- `status`: `todo`, `in-progress`, or `done`
- `createdAt`: Task creation timestamp
- `updatedAt`: Last update timestamp

---

# Project Details
- The **command-line prompt** will use the `input()` function.
- Tasks will be stored in a `.json` file.

---

## **Project URL**
https://roadmap.sh/projects/task-tracker
