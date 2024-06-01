from django.urls import path,include
from . import views

urlpatterns = [
    path('add_department', views.add_department, name='add_departments'),
    path('addstudent', views.add_student, name='add_student'),
    path('listdepartment', views.list_students_by_department, name='listdeparment'),
    path('', views.department_list, name='alldepartment'),
    path('updatdepartment/<int:pk>/update/', views.update_department, name='update_department'),
    path('department/<int:pk>/delete/', views.delete_department, name='delete_department'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path('student/<int:pk>/update/', views.update_student, name='update_student'),
    path('student_list', views.student_list, name='student_list'),









]
