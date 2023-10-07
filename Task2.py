import pickle

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def delete_task(self, task_title):
        for task in self.tasks:
            if task.title.lower() == task_title.lower():
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    def save_tasks(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.tasks, file)
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"Error occurred while saving tasks: {e}")

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
            print("Tasks loaded successfully.")
        except Exception as e:
            print(f"Error occurred while loading tasks: {e}")


def display_menu():
    print("===== To-Do List App =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")


def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == '2':
            title = input("Enter task title to delete: ")
            todo_list.delete_task(title)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == '5':
            filename = input("Enter filename to load tasks: ")
            todo_list.load_tasks(filename)
        elif choice == '6':
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()