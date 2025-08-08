from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'items': items})

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        created_at = request.POST.get('created_at')
        completed_at = request.POST.get('completed_at')
        if task:
            TodoItem.objects.create(task=task, created_at=created_at, completed_at=completed_at)
    return redirect('todo_list')

def edit(request, id):
    item = TodoItem.objects.get(id=id)
    if request.method == 'POST':
        item.task = request.POST.get('task')
        item.created_at = request.POST.get('created_at')
        item.completed_at = request.POST.get('completed_at')
        item.save()
        return redirect('todo_list')
    return render(request, 'edit_h.html', {'data': item})

def delete_todo(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.delete()
    return redirect('todo_list')
