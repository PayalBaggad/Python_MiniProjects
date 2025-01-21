# A program to create and manage a simple to-do list.

def todo_list():
    tasks = []
    
    while True:
        print("\nTo-Do List Options:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            print("\nYour tasks:")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks found.")
        elif choice == '3':
            task_no = int(input("Enter the task number to delete: "))
            if 0 < task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

todo_list()

"""
Explanation:
1. The program maintains a list of tasks (tasks).
2. Users can:
    A. Add a task: Enter a task to be added to the list.
    B. View tasks: Display the list of tasks with numbering.
    C. Delete a task: Remove a task based on its number.
    D. Exit: Stop the program.
4. Input validation ensures tasks are managed correctly.
"""
