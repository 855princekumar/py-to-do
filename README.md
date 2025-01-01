# py-to-do

Welcome to the py-to-do repository! 📝✨

## Overview

This repository contains a simple To-Do List web application built using **PHP**, **Python**, **JSON**, and **AJAX** for task management. The app allows users to add and delete tasks, and the task list is saved persistently without refreshing the page.

## Tech Stack

- **PHP:** Used for the frontend to handle user inputs and requests. It processes form submissions and interacts with the backend Python script.
- **Python:** Handles backend logic, processing task management requests, and updates a **JSON** file to store the tasks.
- **JSON:** Used as a lightweight data format to store the task list, allowing persistence across page reloads.
- **AJAX:** Ensures smooth task updates without the need for a page refresh, providing a seamless user experience.

### How It Works

- The **PHP** frontend manages the user interface and handles form submissions. It sends task management requests (add or delete tasks) to the **Python** script.
- The **Python** script processes these requests by reading and modifying the **JSON** file, ensuring that tasks persist even after page reloads.
- **AJAX** enables dynamic task updates by exchanging data in **JSON** format, avoiding the need to reload the page and making the experience more responsive and efficient.

### Advantages:

- Efficient task handling with minimal server load.
- Real-time task updates without page refresh.
- Data persistence with JSON-based storage for easy scalability.
- Seamless integration of frontend and backend using PHP and Python.
- AJAX ensures a smooth, user-friendly experience.

## Features

- **Add Tasks:** Quickly add new tasks to your to-do list.
- **Delete Tasks:** Remove tasks from the list with a click.
- **Persistent Storage:** Task data is saved across page reloads using Python and JSON.
- **User-Friendly Interface:** Enjoy a clean and intuitive interface.

## How to Use

1. **Adding Tasks:** Type your task into the input field at the top and press "Add".
2. **Deleting Tasks:** Click on a task in the list and press "Delete" to remove it.
3. The task list will update dynamically without refreshing the page.

## Installation

### Windows (Using XAMPP):

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/855princekumar/py-to-do.git
    ```

2. Navigate to the project directory:

    ```bash
    cd py-to-do
    ```

3. Run the application:

    ```bash
    php -S localhost:8000
    ```

The app will be accessible in your browser on [http://localhost:8000](http://localhost:8000).

### Linux (Using Apache Server):

1. Clone the repository to your machine:

    ```bash
    git clone https://github.com/855princekumar/py-to-do.git
    ```

2. Move the project directory to the Apache server's root directory:

    ```bash
    sudo mv py-to-do /var/www/html/
    ```

3. Change the directory permissions to allow access:

    ```bash
    sudo chown -R www-data:www-data /var/www/html/py-to-do
    sudo chmod -R 755 /var/www/html/py-to-do
    ```

4. Restart the Apache server:

    ```bash
    sudo systemctl restart apache2
    ```

The app will be accessible in your browser on [http://localhost/py-to-do](http://localhost/py-to-do).

## Contributions

Contributions to enhance the functionality or fix issues are welcome. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Create a new Pull Request.

## Requirements

- PHP 7.x or above
- Python 3.x
- A web browser
- Apache Server (for Linux)

## License

This project is licensed under the **Apache License 2.0**. You may use, modify, and distribute the code in accordance with the terms of the license.

