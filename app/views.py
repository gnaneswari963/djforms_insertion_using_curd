from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *

# Create your views here.

def djforms(request):

    ENFO=NameForm()
    d={'ENFO':ENFO}

    if request.method=='POST':
        NFDO=NameForm(request.POST)
        if NFDO.is_valid():
            return  HttpResponse(str(NFDO.cleaned_data))
            #return  HttpResponse(NFDO.cleaned_data)
            #return  HttpResponse(NFDO.cleaned_data['Sname'])
        else:
            return HttpResponse('data is invalid') 
    return render(request,'djforms.html',d)


def student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            #return HttpResponse(SFDO.cleaned_data)
            #return HttpResponse(SFDO.cleaned_data['Sage'])
            return HttpResponse(str(SFDO.cleaned_data))

        else:
            return('data is invalid')
    return render(request,'student.html',d)

def insert_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['sname']
            sa=SFDO.cleaned_data['sage']
            sg=SFDO.cleaned_data['sgender']
            sc=SFDO.cleaned_data['scourse']
            sadd=SFDO.cleaned_data['saddress']
            sp=SFDO.cleaned_data['spassword']
            SO=Student.objects.get_or_create(sname=sn,sage=sa,sgender=sg,scourse=sc,saddress=sadd,spassword=sp)
            QLSO=Student.objects.all()
            d1={'QLSO':QLSO}
            return render(request,'display_insert_student.html',d1)
        else:
            return HttpResponse('data is invalid')
    return render(request,'insert_student.html',d)