from django.shortcuts import render

# Create your views here.
from app.models import *

from django.http import HttpResponse

def input_course(request):
    cid=int(input('Enter cid'))
    cname=input('Enter cname')
    C=COURSE.objects.get_or_create(cid=cid)[0]
    C.save()
    return HttpResponse('Data inserted to Course table successfully')
def input_student(request):
    cid=int(input('enter cid'))
    sname=input('enter cname')
    email=input('enter email')
    CT=COURSE.objects.filter(cid=cid)
    if CT:
       CTO=CT[0]
       SO=STUDENT.objects.get_or_create(cid=CTO,sname=sname,email=email)[0]
       SO.save()
       return HttpResponse('data entered to student table succesfully')
    else:
        return HttpResponse('Given data is not present in parent table') 
    