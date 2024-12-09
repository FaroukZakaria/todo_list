// Add a new task
async function addTask(event) {
    event.preventDefault();
    const title = document.getElementById('task-title').value;
    const response = await fetch('tasks/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title }),
    });
    if (response.ok) {
        document.getElementById('task-title').value = '';
        fetchTasks();
    } else {
        alert('Failed to add task!');
    }
}