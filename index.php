<?php
// Path to the Python script
$pythonScript = "todo_app.py";

// Function to execute the Python script and get JSON response
function runPythonScript($action, $argument = null) {
    global $pythonScript; // Ensure the variable is accessible
    $command = escapeshellcmd("python $pythonScript $action " . escapeshellarg($argument));
    $output = shell_exec($command);
    return json_decode($output, true);
}

// Handle POST requests from AJAX
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'] ?? null;

    if ($action === 'add') {
        $task = $_POST['task'] ?? '';
        if (!empty($task)) {
            runPythonScript('add', $task);
        }
    } elseif ($action === 'delete') {
        $index = $_POST['index'] ?? -1;
        runPythonScript('delete', $index);
    }

    // Return the updated task list as JSON response
    $response = runPythonScript('');
    echo json_encode($response['tasks']);
    exit;
}

// Fetch all tasks to display (for initial page load)
$response = runPythonScript('');
$tasks = $response['tasks'] ?? [];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>To-Do List</h1>
    <div class="container">
        <form class="task-form" id="taskForm">
            <input type="text" id="taskInput" placeholder="Enter a task..." required>
            <button type="submit">Add</button>
        </form>
        <ul class="task-list" id="taskList">
            <?php foreach ($tasks as $index => $task): ?>
                <li data-index="<?php echo $index; ?>">
                    <?php echo ($index + 1) . '. ' . htmlspecialchars($task); ?>
                    <button class="delete-task">Delete</button>
                </li>
            <?php endforeach; ?>
        </ul>
    </div>
    <br>
    <div class="description">
        <p><strong>Tech Stack:</strong> PHP, Python, JSON, and AJAX</p>
        <p><strong>How It Works:</strong> The frontend, built with PHP, interacts with Python for backend task management.</p>
        <p>Data is exchanged in JSON format, while AJAX handles smooth task updates without page reloads, ensuring a dynamic and seamless user experience.</p>
        <p><strong>Advantages:</strong></p>
        <ul>
            <li>Efficient task handling with minimal server load.</li>
            <li>Real-time task updates without page refresh.</li>
            <li>Data persistence with JSON-based storage for easy scalability.</li>
            <li>Seamless integration of frontend and backend using PHP and Python.</li>
            <li>AJAX ensures a smooth, user-friendly experience.</li>
        </ul>
    </div>
    <script src="scripts.js"></script>
</body>
</html>
