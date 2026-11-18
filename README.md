

\# Student Task Manager



A simple Python-based console application for managing daily tasks. This project demonstrates Python programming, Git, GitHub collaboration, branching, unit testing, and GitHub Actions.



\## Features



\- Add new tasks.

\- Display all tasks.

\- Reject empty task titles.

\- Reject task titles longer than 100 characters.

\- Mark tasks as completed.

\- Prevent completing an already completed task.

\- Delete tasks using task IDs.

\- Validate task IDs.

\- Automated unit testing with Python unittest.

\- GitHub Actions for continuous integration.



\## Technologies Used



\- Python 3.11

\- Git

\- GitHub

\- Python unittest

\- GitHub Actions



\## Project Structure



```text

studenttaskmanager/

│

├── .github/

│   └── workflows/

│       └── python-tests.yml

│

├── tests/

│   └── test\_task\_manager.py

│

├── task\_manager.py

├── project\_status.txt

├── README.md

├── LICENSE

└── .gitignore

```



\## Installation



1\. Clone the repository:



&nbsp;  git clone https://github.com/amamashoukat55/studenttaskmanager.git



2\. Open the project folder:



&nbsp;  cd studenttaskmanager



3\. Make sure Python 3.11 or later is installed.



\## Usage



Run the application:



&nbsp;  python task\_manager.py



Choose an option from the menu:



1\. Add Task

2\. Display Tasks

3\. Complete Task

4\. Delete Task

5\. Exit



Follow the instructions displayed in the terminal.



\## Running Unit Tests



Run the following command:



&nbsp;  python -m unittest discover -s tests -v



The tests check:



\- Adding a task.

\- Rejecting an empty task.

\- Completing a task.

\- Deleting a task.



\## GitHub Actions



GitHub Actions automatically runs the unit tests when:



\- Code is pushed to the main branch.

\- A pull request targets the main branch.



The workflow is located at:



.github/workflows/python-tests.yml



\## Version



Current release: v1.0.0



\## Author



Amama Shoukat



