from django.http import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'importData.html')

def importData(request):
    File = pd.ExcelFile(request.FILES['excel'])
    print(File.sheet_names)
    return redirect(to='')




