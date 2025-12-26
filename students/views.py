from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



@login_required
def student_list(request):
    students = Student.objects.filter(user=request.user)
    return render(request, 'students/student_list.html', {'students': students})




@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user   # 🔥 THIS LINE
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})


@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id, user=request.user)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {'form': form})


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id, user=request.user)
    student.delete()
    return redirect('student_list')



@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
