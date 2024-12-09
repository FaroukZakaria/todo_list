# Todo list Application
## Objective
This is a simple to-do list application built using Django. The application allows users to:

1. Add new tasks.
2. View a list of tasks.

### Backend Development (Django)

Functionality implemented includes:
- Adding tasks.
- Viewing a list of tasks.

### Frontend (HTML/CSS)

Basic HTML and CSS are used to create:
- A form to add tasks.
- A list view displaying tasks.

## Setting up the project
To set up the project, follow these steps:
Make sure you have Django installed first before you set up the project:
```bash
pip install django
```

Make a new project:
```bash
django-admin startproject todolist
cd todolist
```

1. **Create a new Django app**:
    ```bash
    python manage.py startapp tasks
    ```

2. **Configure settings**:
    - Add the `static` and `templates` directories in the root directory.
    - Update `settings.py` to include the following configurations:
      ```python
      STATICFILES_DIRS = [
            BASE_DIR / 'static',  # Points to your "static" directory
      ]
      ```
      - Add the `templates` directory to the `DIRS` list in the `TEMPLATES` setting:
      ```python
      TEMPLATES = [
            {
                 # ...
                 'DIRS': [BASE_DIR / 'templates'],
                 # ...
            },
      ]
      ```

3. **Set up URLs**:
    - Create the necessary URLs for the application:
      ```python
      from django.urls import path, include

      urlpatterns = [
            path('', include('tasks.urls')),
            path('tasks/', include('tasks.urls')),
      ]
      ```

4. **Create URL configurations for the `tasks` app**:
    - In `tasks/urls.py`:
      ```python
      from django.urls import path
      from . import views

      urlpatterns = [
            path('', views.index, name='index'),
            path('tasks/', views.task_list, name='task_list'),
            path('tasks/add', views.add_task, name='add_task'),  # API usage to add a task
      ]
      ```

5. **Add a `.gitignore` file**:
    - Create a `.gitignore` file to exclude unwanted files:
      ```
      *.pyc
      __pycache__/
      db.sqlite3
      /static/
      /media/
      ```

Now your project should be set up and ready to use.

## Usage

To run the server, execute the following command:
```bash
python manage.py runserver
```

Then, open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the index (home) page.

To add a task, enter the title in the input box and click "Add Task".

To view the tasks page, go to [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks).
