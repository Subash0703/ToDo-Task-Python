class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nPriority: {self.priority}\nStatus: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, task_id, title, description, priority, status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                task.priority = priority
                task.status = status
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def view_all_tasks(self):
        return self.tasks

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        return filtered_tasks


def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Filter Tasks by Priority")
    print("6. Exit")


def main():
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            priority = input("Enter Priority (High/Medium/Low): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            new_task = Task(task_id, title, description, priority, status)
            task_manager.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            task_id = input("Enter Task ID to edit: ")
            task = task_manager.get_task_by_id(task_id)
            if task:
                title = input("Enter new Title: ")
                description = input("Enter new Description: ")
                priority = input("Enter new Priority (High/Medium/Low): ")
                status = input("Enter new Status (Pending/In Progress/Completed): ")
                task_manager.edit_task(task_id, title, description, priority, status)
                print("Task edited successfully!")
            else:
                print("Task not found.")

        elif choice == "3":
            task_id = input("Enter Task ID to delete: ")
            if task_manager.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task not found.")

        elif choice == "4":
            tasks = task_manager.view_all_tasks()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks found.")

        elif choice == "5":
            priority = input("Enter Priority to filter (High/Medium/Low): ")
            filtered_tasks = task_manager.filter_tasks_by_priority(priority)
            if filtered_tasks:
                for task in filtered_tasks:
                    print(task)
            else:
                print("No tasks found with the specified priority.")

        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()

# Documentation :
# Title: Task Manager Application Documentation
#
# Introduction:
# The Task Manager application facilitates effective task management through a command-line interface.
#
# Functional Requirements:
# 1. Adding Tasks: Users can add tasks with details like title, description, priority, and status.
# 2. Editing Tasks: Users can modify existing tasks by specifying the task ID and providing updated information.
# 3. Deleting Tasks: Users can remove tasks by specifying the task ID.
# 4. Viewing Tasks: Users can see a list of all tasks along with their details.
# 5. Filtering Tasks: Users can filter tasks based on priority levels.
#
# Class Structure:
# 1. Task Class:
#    - Attributes: task_id, title, description, priority, status.
#    - Methods: __init__(), __str__().
#
# 2. TaskManager Class:
#    - Attributes: tasks (list of Task objects).
#    - Methods: __init__(), add_task(), edit_task(), delete_task(),
#               get_task_by_id(), view_all_tasks(), filter_tasks_by_priority().
#
# User Interaction:
# - The application provides a command-line interface for user interaction.
# - Users are presented with a menu containing options to perform various tasks
#   (add, edit, delete, view all tasks, filter tasks by priority, exit).
# - Users input their choice by entering a corresponding number.
#
# Error Handling:
# - The application handles invalid inputs such as incorrect task IDs or priority/status values.
# - Error messages are displayed to guide users in correcting input errors.
#
# Code Implementation:
# - The code consists of two classes: Task and TaskManager.
# - The main() function initializes a TaskManager object and handles
#   user interaction through a menu-driven command-line interface.
# - Users can perform tasks like adding, editing, deleting, viewing, and filtering tasks based on priority levels.
# - Error handling is implemented to handle invalid user inputs and display appropriate error messages.
#
# Usage:
# - Run the script and follow the on-screen instructions to interact with the Task Manager application.
# - Use the menu options to perform various tasks related to task management.
#
# Note:
# - This documentation provides an overview of the Task Manager application and its implementation details.
#
# - Further customization and enhancements can be made based on specific requirements and use cases.

