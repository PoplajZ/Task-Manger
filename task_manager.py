class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def edit_task(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} - {self.description} ({status})"


class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks or []

    def add_task(self, title, description):
        for task in self.tasks:
            if task['title'] == title:
                print("Error: A task with the same title already exists.")
                return

        self.tasks.append({'title': title, 'description': description, 'completed': False})
        print(f"Task '{title}' added successfully.")

    def remove_task_by_name(self, title):
        for task in self.tasks:
            if task['title'] == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed successfully.")
                return
        print(f"Error: Task '{title}' not found.")

    def edit_task_by_name(self, old_title, new_title, new_description):
        for task in self.tasks:
            if task['title'] == old_title:
                task['title'] = new_title
                task['description'] = new_description
                print(f"Task '{old_title}' edited successfully.")
                return
        print(f"Error: Task '{old_title}' not found.")

    def mark_task_completed_by_name(self, title):
        for task in self.tasks:
            if task['title'] == title:
                task['completed'] = True
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Error: Task '{title}' not found.")

    def list(self):
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print(f"- {task['title']}{' (Completed)' if task['completed'] else ''}: {task['description']}")
        else:
            print("No tasks found.")
