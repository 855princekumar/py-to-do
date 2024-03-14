# To-Do List with Python GUI

Welcome to the To-Do List repository! 📝✨

## Overview

This repository contains a simple To-Do List application built using Python and featuring a graphical user interface (GUI) for easy interaction.

![ToDo List Preview](https://github.com/855princekumar/to-do-list/blob/main/to%20do%20list.png)

## Features

- **Add Tasks:** Quickly add new tasks to your to-do list.
- **Delete Tasks:** Remove tasks from the list with a click.
- **User-Friendly Interface:** Enjoy a clean and intuitive interface.
- **Save and Load:** Save your to-do list to a file for later use.

## How to Use

1. **Adding Tasks:** Type your task into the input field at the top and press "Add Task".
2. **Deleting Tasks:** Click on a task in the list and press "Delete Task" to remove it.
3. **Saving and Loading:** Use the "Save List" and "Load List" buttons to manage your tasks across sessions.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/855princekumar/todo-list-python-gui.git
```

2. Navigate to the project directory:

```bash
cd todo-list-python-gui
```

3. Run the application:

```bash
python todo_list.py
```

## Convert to Executable

You can convert the Python code into an executable (.exe) file for easier distribution using `pyinstaller`. Follow these steps:

1. Ensure `pyinstaller` is installed:

```bash
pip install pyinstaller
```

2. Navigate to the directory containing your Python script (`todo_list.py`) in the command prompt or terminal.

3. Run the following command to create the executable:

```bash
pyinstaller --onefile todo_list.py
```

This command will create a `dist` directory containing the executable file. The `--onefile` flag bundles everything into a single executable file.

## Contributions

Contributions to enhance the functionality or fix issues are welcome. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Create a new Pull Request.

## Requirements

- Python 3.x
- Tkinter
- pyinstaller

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this code for your purposes.

Happy task managing! 🚀
