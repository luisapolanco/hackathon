from django.http import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd
from .models import Course, Student

# Create your views here.
def home(request):
    return render(request, 'importData.html')

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
            #     Course.create_course(id_course=user_course)
            # Student.create_student(user_email, user_id, user_name, user_course)

        
        
    
    return redirect(to='/')




