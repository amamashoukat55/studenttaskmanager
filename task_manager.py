class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = {
            "id": self.next_id,
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n--- Student Tasks ---")

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f'{task["id"]}. {task["title"]} - {status}')

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print("Task marked as completed!")
                return True

        print("Task ID not found.")
        return False


def main():
    manager = TaskManager()

    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.display_tasks()

        elif choice == "3":
            manager.display_tasks()

            try:
                task_id = int(input("Enter task ID to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid numeric task ID.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()