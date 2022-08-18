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
        total = table.objects.get(seatNumber=st)
        mytotal = total.arabic + total.english + total.math + total.social + total.sience + total.islamic + total.olenglish + total.computer + total.art
        percntage = round(mytotal / 480 * 100 ,1)
        context={'students':table.objects.get(seatNumber=st),'total':mytotal,'percnt':percntage}
        return render(request,'searchdb/natega.html',context)
    except:
        Error ={'error_message':'* ﻻ توجد نتائج تأكد من رقم الجلوس'}
        return render(request,'searchdb/index.html',Error)
    
   

