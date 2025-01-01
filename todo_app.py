import sys
import json
import os

# File to store tasks persistently
TASKS_FILE = "tasks.json"

# Load tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return tasks

# Delete a task by index
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return tasks

# Main entry point for the script
if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else None
    if action == "add":
        task = sys.argv[2] if len(sys.argv) > 2 else None
        if task:
            tasks = add_task(task)
            print(json.dumps({"status": "success", "tasks": tasks}))
        else:
            print(json.dumps({"status": "error", "message": "Task content required"}))
    elif action == "delete":
        index = int(sys.argv[2]) if len(sys.argv) > 2 else -1
        if index >= 0:
            tasks = delete_task(index)
            print(json.dumps({"status": "success", "tasks": tasks}))
        else:
            print(json.dumps({"status": "error", "message": "Valid task index required"}))
    else:
        # Default: Return all tasks
        tasks = load_tasks()
        print(json.dumps({"status": "success", "tasks": tasks}))
