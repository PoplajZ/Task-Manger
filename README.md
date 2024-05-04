# Task Manager

The Task Manager is a simple command-line application written in Python. It provides a convenient way to manage your tasks, allowing you to add, remove, edit, mark as completed, and display tasks.

## Installation

To use the Task Manager, follow these steps:

1. Clone this repository to your local machine:

```git clone https://github.com/your-username/task-manager```

2. Navigate to the project directory:

```cd task-manager```

3. Install the required dependencies:

```pip install -r requirements.txt```

## Features

### Add Task
You can add a new task with a title and description. If a task with the same title already exists, the program will notify you and prevent duplicate tasks from being added.

### Remove Task
You can remove a task by specifying its title. If the task exists, it will be removed from the list of tasks. If the task does not exist, an error message will be displayed.

### Edit Task
You can edit an existing task by specifying its title. You can change the title and description of the task. If the task exists, it will be updated with the new information. If the task does not exist, an error message will be displayed.

### Mark Task as Completed
You can mark a task as completed by specifying its title. If the task exists, it will be marked as completed. If the task does not exist, an error message will be displayed.

### List Tasks
You can display all tasks currently stored in the Task Manager. Each task is displayed with its title, description, and completion status.

### Clear Screen
You can clear the command-line interface to improve readability.

### Exit Program
You can exit the Task Manager, and all tasks will be saved to a file for future use.

## Usage

1. Run the program by executing `python main.py` in your terminal.
2. Use the following commands to interact with the Task Manager:
   - `addtask <title>`: Add a new task with the specified title.
   - `removetask <title>`: Remove the task with the specified title.
   - `edittask <title>`: Edit the task with the specified title.
   - `markcompleted <title>`: Mark the task with the specified title as completed.
   - `list`: Display all tasks.
   - `clear`: Clear the screen.
   - `exit`: Exit the program.
   - `help`: Display available commands.
3. Follow the on-screen prompts to provide additional information when necessary.

---

