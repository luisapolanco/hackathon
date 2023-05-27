from django.http import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd
from .models import Course, Student
from .forms import monitoringWorkshopForm
from .models import Supplementary

# Create your views here.
def home(request):
    return render(request, 'importData.html')

def confirmMonitoringWorkshop(request):
    estudiantes = Supplementary.objects.all()
    if request.method == 'POST':
        form = monitoringWorkshopForm(request.POST, request.FILES)

        if form.is_valid():
            if form.is_valid():
                form.save()
                return redirect('profesor.html')  

    else:
        form = monitoringWorkshopForm()

    return render(request, 'profesor.html', {'form': form,'estudiantes':estudiantes})

def importData(request):
    File = pd.ExcelFile(request.FILES['excel'])
    df=File.parse('Sheet1')
    for item in df.index:
        for itemColumn in df.columns:
            user_name = df.at[item, 'Nombre y Apellido']
            user_id = df.at[item, 'ID EAFIT']
            user_email = df.at[item, 'Correo institucional']
            user_course = df.at[item, 'Número del código del Grupo']
            courseExists = Course.objects.filter(id=user_course).exists()
            if(courseExists == False):
                course = create_course(id_course=user_course)
            student = create_student(user_email, user_id, user_name, course)
            stude = Student.objects.get(id=student.id)
            stu = Student()
            stu.id = stude.id
            stu.name = stude.name
            stu.id_course = stude.id_course
            sup = create_supplementary(stu, course)
    return redirect(to='/')


def create_student(email, id, name,  course):
    user = Student()
    user.id = id,
    user.email = email, 
    user.name = name, 
    user.id_course = course      
    user.save()
    return user

def create_course(id_course):
    course = Course()
    course.id = id_course,
    course.name = "Calculo"
    course.save()
    return course


def create_supplementary(student, id_course ):
    sup = Supplementary()
    sup.id_student = student,
    sup.id_course = id_course
    sup.save()
    return sup


def mainEstudiante(request):
    return render(request, 'estudiante.html')

def supletorioEstudiante(request):
    return render(request, 'estudiante2.html')

def monitoriaEstudiante(request):
    return render(request, 'estudiante3.html')

def tallerEstudiante(request):
    return render(request, 'estudiante4.html')
