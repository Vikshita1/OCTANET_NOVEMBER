tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def list_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task name: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        list_tasks()
        task_index = int(input("Enter the task index to mark as completed: "))
        complete_task(task_index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")

print("Goodbye!")