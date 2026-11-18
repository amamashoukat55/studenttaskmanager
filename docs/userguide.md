

\# Student Task Manager - User Guide



\## 1. Introduction



Student Task Manager is a Python console application that helps users organize and manage their tasks.



Users can add, display, complete, and delete tasks through a simple menu.



\## 2. Requirements



Before running the application, make sure you have:



\- Python 3.11 or later

\- Git (optional, for cloning the project)

\- A terminal or command prompt



\## 3. Getting Started



Clone the repository:



```bash

git clone https://github.com/amamashoukat55/studenttaskmanager.git

```



Open the project directory:



```bash

cd studenttaskmanager

```



\## 4. Running the Application



Run this command:



```bash

python task\_manager.py

```



On Windows, you can also use:



```bash

py task\_manager.py

```



\## 5. Application Menu



The application provides five options:



\### Option 1: Add Task



\- Select Add Task.

\- Enter a task title.

\- The application rejects empty titles.

\- Task titles cannot exceed 100 characters.



\### Option 2: Display Tasks



\- Select Display Tasks.

\- All existing tasks and their completion status are displayed.



\### Option 3: Complete Task



\- Select Complete Task.

\- Enter the task ID.

\- The selected task is marked as completed.

\- An already completed task cannot be completed again.



\### Option 4: Delete Task



\- Select Delete Task.

\- Enter the task ID.

\- The selected task is deleted if the ID is valid.



\### Option 5: Exit



Select Exit to close the application.



\## 6. Running Unit Tests



To run the automated tests, execute:



```bash

py -m unittest discover -s tests -v

```



The test suite checks:



\- Adding a valid task.

\- Rejecting an empty task.

\- Completing a task.

\- Deleting a task.



\## 7. GitHub Actions



The project uses GitHub Actions to run unit tests automatically.



Tests execute when code is pushed to the main branch or when a pull request targets main.



The workflow file is:



`.github/workflows/python-tests.yml`



\## 8. Troubleshooting



\- If Python is not recognized, try `py` instead of `python`.

\- If a task title is empty, enter a valid title.

\- If a task ID is invalid, enter an existing positive task ID.

\- If tests fail, read the error message and check the relevant code.



\## 9. Project Repository



GitHub:



https://github.com/amamashoukat55/studenttaskmanager



