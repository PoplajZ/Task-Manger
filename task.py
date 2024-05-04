class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def edit_task(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} - {self.description} ({status})"
