import os
from task_manager import TaskManager
from file_manager import FileManager
from colorama import init, Fore

def print_welcome_message():
    welcome_message = """

  _______        _____ _  __     __  __          _   _          _____ ______ _____  
 |__   __|/\    / ____| |/ /    |  \/  |   /\   | \ | |   /\   / ____|  ____|  __ \ 
    | |  /  \  | (___ | ' /     | \  / |  /  \  |  \| |  /  \ | |  __| |__  | |__) |
    | | / /\ \  \___ \|  <      | |\/| | / /\ \ | . ` | / /\ \| | |_ |  __| |  _  / 
    | |/ ____ \ ____) | . \     | |  | |/ ____ \| |\  |/ ____ \ |__| | |____| | \ \ 
    |_/_/    \_\_____/|_|\_\    |_|  |_/_/    \_\_| \_/_/    \_\_____|______|_|  \_\
                                                                                    
                                                                                    

    """
    print(Fore.GREEN + welcome_message + Fore.RESET)

def print_help():
    print(Fore.YELLOW + "Available commands:" + Fore.RESET)
    print("")
    print(Fore.GREEN + "addtask <title>:" + Fore.RESET + " Add a new task with the given title.")
    print(Fore.GREEN + "rmtask <title>:" + Fore.RESET + " Remove a task with the given title.")
    print(Fore.GREEN + "edittask <title>:" + Fore.RESET + " Edit an existing task with the given title.")
    print(Fore.GREEN + "markcompleted <title>:" + Fore.RESET + " Mark a task as completed with the given title.")
    print(Fore.GREEN + "list:" + Fore.RESET + " Display all tasks.")
    print(Fore.GREEN + "clear:" + Fore.RESET + " Clear the screen.")
    print(Fore.GREEN + "help:" + Fore.RESET + " Display available commands.")
    print(Fore.GREEN + "exit:" + Fore.RESET + " Exit the program.")
    

def main():
    init(autoreset=True)  # Initialize colorama
    print_welcome_message()

    file_manager = FileManager("tasks.pkl")
    tasks = file_manager.load_tasks()
    task_manager = TaskManager(tasks)

    print_help()

    while True:
        command = input(Fore.BLUE + "> " + Fore.RESET).strip().lower()

        if command.startswith("addtask"):
            _, title = command.split(maxsplit=1)
            description = input(Fore.BLUE + "Enter task description: " + Fore.RESET)
            task_manager.add_task(title, description)
        elif command.startswith("rmtask"):
            _, title = command.split(maxsplit=1)
            task_manager.remove_task_by_name(title)
        elif command.startswith("edittask"):
            _, title = command.split(maxsplit=1)
            new_title = input(Fore.BLUE + "Enter new task title: " + Fore.RESET)
            new_description = input(Fore.BLUE + "Enter new task description: " + Fore.RESET)
            task_manager.edit_task_by_name(title, new_title, new_description)
        elif command.startswith("markcompleted"):
            _, title = command.split(maxsplit=1)
            task_manager.mark_task_completed_by_name(title)
        elif command == "list":
            task_manager.list()
        elif command == "clear":
            os.system("cls" if os.name == "nt" else "clear")
        elif command == "exit":
            file_manager.save_tasks(task_manager.tasks)
            print(Fore.YELLOW + "Exiting program." + Fore.RESET)
            break
        elif command == "help":
            print_help()
        else:
            print(Fore.RED + "Invalid command. Type 'help' to see available commands." + Fore.RESET)

if __name__ == "__main__":
    main()
