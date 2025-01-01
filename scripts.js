// Function to handle adding tasks without refreshing
document.getElementById('taskForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const taskInput = document.getElementById('taskInput');
    const taskText = taskInput.value.trim();

    if (taskText) {
        const formData = new FormData();
        formData.append('action', 'add');
        formData.append('task', taskText);

        fetch('index.php', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                updateTaskList(data);  // Update task list without refreshing
            });

        taskInput.value = '';  // Clear input field
    }
});

// Function to delete a task
document.getElementById('taskList').addEventListener('click', function (event) {
    if (event.target.classList.contains('delete-task')) {
        const li = event.target.closest('li');
        const index = li.dataset.index;

        const formData = new FormData();
        formData.append('action', 'delete');
        formData.append('index', index);

        fetch('index.php', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                updateTaskList(data);  // Update task list without refreshing
            });
    }
});

// Function to update the task list dynamically
function updateTaskList(tasks) {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';

    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.dataset.index = index;
        li.innerHTML = `${index + 1}. ${task} <button class="delete-task">Delete</button>`;
        taskList.appendChild(li);
    });
}
