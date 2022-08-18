from django.shortcuts import render
from .models import Student,Student2
from django.http import HttpResponse
# Create your views here.
def index(request):
    
    return render(request,'searchdb/index.html')


def natega(request):
    if request.method == 'POST':
     st = request.POST.get('seatnumber')
     mar7la = request.POST.get('mra7el')

    if mar7la == '1':
        table = Student
    if mar7la == '2':
        table = Student2

    try:
        context={'students':table.objects.get(seatNumber=st)}
        return render(request,'searchdb/natega.html',context)
    except:
        Error ={'error_message':'* ﻻ توجد نتائج تأكد من رقم الجلوس'}
        return render(request,'searchdb/index.html',Error)
    
   

