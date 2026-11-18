class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not title.strip():
            print("Error: Task title cannot be empty.")
            return False

        if len(title.strip()) > 100:
            print("Error: Task title must be 100 characters or fewer.")
            return False

        task = {
            "id": self.next_id,
            "title": title.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully!")
        return True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n--- Student Tasks ---")

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f'{task["id"]}. {task["title"]} - {status}')


def main():
    manager = TaskManager()

    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.display_tasks()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()