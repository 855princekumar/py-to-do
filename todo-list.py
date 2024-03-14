# Import the tkinter module and alias it as tk for easier reference
import tkinter as tk
# Import the messagebox module from tkinter for displaying warning messages
from tkinter import messagebox

# Define a class TodoApp
class TodoApp:
    # Constructor method to initialize the application
    def __init__(self, root):
        # Store the root window object
        self.root = root
        # Set the title of the root window
        self.root.title("To-Do List")
        # Set the dimensions of the root window
        self.root.geometry("400x500")
        # Set the background color of the root window
        self.root.configure(bg="#333")

        # Create a frame with rounded corners
        self.frame = tk.Frame(root, bg="#333", bd=5, relief=tk.GROOVE)
        # Place the frame in the center of the root window
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a larger input text field
        self.task_entry = tk.Entry(self.frame, font=("Arial", 14), bg="#444", fg="#fff", insertbackground="#fff")
        # Pack the input field with padding and increased height (ipady)
        self.task_entry.pack(pady=10, padx=10, fill=tk.X, ipady=8)

        # Create a button for adding tasks
        add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#555", fg="#fff")
        # Pack the add button
        add_button.pack(pady=5, padx=10, fill=tk.X)

        # Create a listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, selectbackground="#555", selectforeground="#fff", font=("Arial", 12), bg="#333", fg="#fff")
        # Pack the listbox with padding and expand it in both directions
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Create a button for deleting tasks
        delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task, font=("Arial", 12), bg="#555", fg="#fff")
        # Pack the delete button
        delete_button.pack(pady=5, padx=10, fill=tk.X)

    # Method to add a new task
    def add_task(self):
        # Get the task text from the input field
        task = self.task_entry.get()
        # Check if the task text is not empty
        if task:
            # Append the task to the tasks list
            self.tasks.append(task)
            # Update the task list display
            self.update_task_list()
            # Clear the input field
            self.task_entry.delete(0, tk.END)
        else:
            # Show a warning message if the task text is empty
            messagebox.showwarning("Warning", "Please enter a task.")

    # Method to delete a task
    def delete_task(self):
        # Get the index of the selected task
        selected_task_index = self.task_listbox.curselection()
        # Check if a task is selected
        if selected_task_index:
            # Remove the selected task from the tasks list
            self.tasks.pop(selected_task_index[0])
            # Update the task list display
            self.update_task_list()
        else:
            # Show a warning message if no task is selected for deletion
            messagebox.showwarning("Warning", "Please select a task to delete.")

    # Method to update the task list display
    def update_task_list(self):
        # Clear the task listbox
        self.task_listbox.delete(0, tk.END)
        # Iterate over the tasks list and display each task with numbering
        for i, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{i}. {task}")

# Main function to run the application
def main():
    # Create the root window
    root = tk.Tk()
    # Set the dimensions of the root window
    root.geometry("400x500")
    # Create an instance of the TodoApp class with the root window as argument
    app = TodoApp(root)
    # Initialize the tasks list
    app.tasks = []
    # Start the tkinter event loop
    root.mainloop()

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()
