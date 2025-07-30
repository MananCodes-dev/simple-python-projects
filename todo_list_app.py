task = []

def show_menu():
    print("/n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task_name = input("Enter the task name:")
    task.append(task_name)
    print(f"Task '{task_name}' added.")

def view_tasks():
    if not task:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task_name in enumerate(task, start=1):
            print(f"{index}. {task_name}")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to remove: "))
        if 0 < index <= len(task):
            removed_task = task.pop(index - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
            print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")