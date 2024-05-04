import pickle

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, "rb") as file:
                tasks = pickle.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' does not exist.")
            tasks = []
        except pickle.UnpicklingError:
            print(f"Error: Unable to load tasks from '{self.filename}'. The file may be corrupted or in an invalid format.")
            tasks = []

        return tasks

    def save_tasks(self, tasks):
        with open(self.filename, "wb") as file:
            pickle.dump(tasks, file)
