
TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from file into a list."""
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save task list back to file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✔ Task added: {task}")


def remove_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"❌ Task removed: {removed}")
    except:
        print("⚠ Invalid task number!")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks available!")
        return

    print("\n📌 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()


def main():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            view_tasks()
            number = int(input("Enter task number to remove: "))
            remove_task(number)

        elif choice == "3":
            view_tasks()

        elif choice == "4":
            print("👋 Exiting... Bye!")
            break

        else:
            print("⚠ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
