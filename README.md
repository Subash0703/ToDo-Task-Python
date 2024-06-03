Documentation :
Title: Task Manager Application Documentation

Introduction:
The Task Manager application facilitates effective task management through a command-line interface.

Functional Requirements:
1. Adding Tasks: Users can add tasks with details like title, description, priority, and status.
2. Editing Tasks: Users can modify existing tasks by specifying the task ID and providing updated information.
3. Deleting Tasks: Users can remove tasks by specifying the task ID.
4. Viewing Tasks: Users can see a list of all tasks along with their details.
5. Filtering Tasks: Users can filter tasks based on priority levels.

Class Structure:
1. Task Class:
   - Attributes: task_id, title, description, priority, status.
   - Methods: __init__(), __str__().

2. TaskManager Class:
   - Attributes: tasks (list of Task objects).
   - Methods: __init__(), add_task(), edit_task(), delete_task(),
              get_task_by_id(), view_all_tasks(), filter_tasks_by_priority().

User Interaction:
- The application provides a command-line interface for user interaction.
- Users are presented with a menu containing options to perform various tasks
  (add, edit, delete, view all tasks, filter tasks by priority, exit).
- Users input their choice by entering a corresponding number.

Error Handling:
- The application handles invalid inputs such as incorrect task IDs or priority/status values.
- Error messages are displayed to guide users in correcting input errors.

Code Implementation:
- The code consists of two classes: Task and TaskManager.
- The main() function initializes a TaskManager object and handles
  user interaction through a menu-driven command-line interface.
- Users can perform tasks like adding, editing, deleting, viewing, and filtering tasks based on priority levels.
- Error handling is implemented to handle invalid user inputs and display appropriate error messages.

Usage:
- Run the script and follow the on-screen instructions to interact with the Task Manager application.
- Use the menu options to perform various tasks related to task management.

Note:
- This documentation provides an overview of the Task Manager application and its implementation details.

- Further customization and enhancements can be made based on specific requirements and use cases.
