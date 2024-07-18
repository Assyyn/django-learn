from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest

from .models import Todo


def index(request):
    context = {'todos': Todo.objects.all()}
    return render(request, 'index.html', context=context)


def create(request: HttpRequest):
    if request.method == 'POST':
        Todo.objects.create(name=request.POST.get('name'), description=request.POST.get(
            'description'), status=request.POST.get('status'))
        return redirect('base:home')
    return render(request, 'create.html')


def edit(request, todo_id):
    to_edit = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        to_edit.name = request.POST.get('name')
        to_edit.description = request.POST.get('description')
        to_edit.status = request.POST.get('status')
        to_edit.save()
        return redirect('base:home')

    return render(request, 'edit.html', {'todo': to_edit})


def delete(request, todo_id):
    to_delete = get_object_or_404(Todo, pk=todo_id)
    to_delete.delete()

    return redirect('base:home')
