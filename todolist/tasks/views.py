from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Task
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
def task_list(request):
    tasks = Task.objects.values('title') # Get dictionaries
    if request.method == 'GET':
        return render(request, 'tasks/task_list.html', {'tasks': tasks})
    return JsonResponse({'tasks': list(tasks)})

@csrf_exempt
@require_http_methods(["POST"])
def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        if title:
            task = Task.objects.create(title=title)
            return JsonResponse({'title': task.title}, status=201)
    return JsonResponse({'error': 'Invalid data'}, status=400)

def frontend(request):
    return render(request, 'tasks/index.html')
