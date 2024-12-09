// Fetch tasks from the backend
async function fetchTasks() {
    const response = await fetch('tasks/', {method: 'POST'});
    const data = await response.json();
    const taskList = document.getElementById('task-list');
    const content = document.getElementById('content');
    taskList.innerHTML = '';
    data.tasks.reverse().forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title;
        
        taskList.appendChild(li);
    });
    content.appendChild(taskList);
}