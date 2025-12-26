from django.shortcuts import render
from .models import Task
from .forms import TaskForm

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'students/task_list.html', {'tasks': tasks})





@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'students/add_task.html', {'form': form})



@login_required
def toggle_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')



@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('task_list')



@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
