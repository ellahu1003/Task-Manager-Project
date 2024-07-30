# Task-manager

## Project Overview
A command-line application in Python that efficiently manages user authentication, task tracking, and administrative functions. It streamlines task management, allowing members of a small business to effortlessly view, manage, and assign tasks internally.

## Technology used
Python

## Dataset
The dataset used for this project is stored in user.txt and tasks.txt files, containing user credentials for the admin and task details, respectively.

## Project Structure
```markdown
task-manager/
│
├── data/
│   └── user.txt
│   └── tasks.txt
│
├── task_manager.py
│
└── README.md
```

## Methodology
1) Data Collection:

The project reads user credentials and task information from text files. The user credentials are stored in 'user.txt', and tasks are stored in 'tasks.txt'. The data for this task manager project is primarily driven by user input.

2) User Authentication:
   1. Reading User Credentials: User credentials are read from the 'user.txt' file and stored in a dictionary user_credentials. The user.txt file contains lines of usernames and passwords separated by commas.
   2. Login Section: Users are prompted to enter their username and password. Two while loops are used to validate the entered credentials against the stored credentials. If the entered username or password is incorrect, the user is prompted to retry until the correct credentials are entered. A success message is displayed upon successful login.

4) Main Menu and User Options:
   1. Register a User ('r'): Users can register a new user by providing a new username and password. Password confirmation is required to ensure accuracy. New user credentials are appended to the 'user.txt' file upon successful registration.
   2. Add Task ('a'): Users can assign a task to any user by providing the username, task title, description, due date, and the date assigned. The new task is appended to the 'tasks.txt' file with a status of "No".
   3. View All Tasks ('va'): All tasks from 'tasks.txt' are read and displayed. Task information such as assigned user, title, description, due date, assigned date, and status is printed for each task.
   4. View My Tasks ('vm'): Tasks assigned to the logged-in user are displayed. Task information such as title, description, due date, assigned date, and status is printed for each relevant task.
   5. Exit ('e'): The program exits with a goodbye message.

5) Error Handling and Validation: 
   1. Input Validation: The menu options are validated to ensure the user enters a valid option. If an invalid input is entered, an error message is displayed, and the user is prompted to try again.
   2. Password Confirmation: When registering a new user, the entered password must be confirmed by re-entering it to avoid mistakes.
   3. Task Information Handling: The task information is split and formatted to be more readable when displaying tasks.

6) User Input Dependency:

The functionality and data management within this project heavily depend on the user's input. Users are responsible for entering valid usernames, passwords, task details, and selecting appropriate menu options to ensure proper operation and data integrity.

## Setup and Installation
1) Clone the repository:
    ```sh
   git clone https://github.com/ellahu1003/task-manager.git
   cd task-manager
    ```
2) Run the application:
    ```sh
    python task_manager.py
    ```

## Requirements
The project does not require any additional packages beyond Python standard libraries.

## Features
1) User Authentication: Secure login for users.
2) Task Management: Add, view, and manage tasks.
3) Administrative Functions: Register new users and assign tasks.
4) Main Menu Options:
```markdown
   r - Register a new user.
   a - Add a new task.
   va - View all tasks.
   vm - View my tasks.
   e - Exit the application.
```

## Conclusion
This Task Manager project provides a simple yet effective solution for managing tasks and user authentication within a small business environment. It allows users to easily assign and track tasks, ensuring efficient workflow and task management.


