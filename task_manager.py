
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not title.strip():
            print("Error: Task title cannot be empty.")
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

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("Task is already completed.")
                    return False

                task["completed"] = True
                print("Task marked as completed!")
                return True

        print("Task ID not found.")
        return False

    def delete_task(self, task_id):
        if task_id <= 0:
            print("Please enter a valid positive task ID.")
            return False

        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
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
        print("4. Delete Task")
        print("5. Exit")

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
            manager.display_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid numeric task ID.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
