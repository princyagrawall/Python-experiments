"""Create a Todo list Manager where users can add, view, and remove tasks. Use
List for storing tasks."""

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added.")


    elif choice == "2":
        print("Your Tasks:")
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            i = 0
            while i < len(tasks):
                print(i+1, ".", tasks[i])
                i = i + 1


    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            num = int(input("Enter task number to remove: "))
            if num > 0 and num <= len(tasks):
                tasks.pop(num-1)
                print("Task Removed.")
            else:
                print("Invalid task number.")


    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
