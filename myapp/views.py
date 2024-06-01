from django.shortcuts import render, redirect
from .models import Department, Student
from .forms import DepartmentForm, StudentForm
from django.shortcuts import render, redirect, get_object_or_404

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = DepartmentForm()
    return render(request, 'myapp/Add_department.html', {'form': form})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listdeparment')
    else:
        form = StudentForm()
    return render(request, 'myapp/Add_student.html', {'form': form})


def list_students_by_department(request):
    departments = Department.objects.all()
    students_by_department = {}
    for department in departments:
        students_by_department[department] = Student.objects.filter(department=department)
    return render(request, 'myapp/list_students_by_department.html', {'students_by_department': students_by_department})



def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('alldepartment')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'myapp/update_department.html', {'form': form})



def department_list(request):
    departments = Department.objects.all()
    return render(request, 'myapp/Departmentlist.html', {'departments': departments})



def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return redirect('alldepartment')


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_list.html', {'students': students})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'myapp/update_student.html', {'form': form})
