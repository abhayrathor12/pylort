from django.shortcuts import render
from . models import * 
from datetime import datetime
from django.http import HttpResponse
from django.db.models.query import Q



def index(request):
    return render(request,'index.html')

def all_stu(request):
    stu=Students.objects.all()
    dict={
        'stu':stu
    }
  
    return render(request,'all_stu.html',dict)


def add_stu(request):

    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        fees=request.POST.get('fees')
        phone=int(request.POST.get('phone'))
        cour=int(request.POST.get('cour'))
        dur=int(request.POST.get('dur'))
        
        new_stu=Students(first_name=first_name,last_name=last_name,fees=fees,phone=phone,cour_id=cour,dur_id=dur,joined_date=datetime.now())
        new_stu.save()
        return HttpResponse("Students add succesfully")
    return render(request,'add_stu.html')


def rem_stu(request):
    stu=Students.objects.all()
    dict={
        "stu":stu
    }
    return render(request,'rem_stu.html',dict)

def remove_stu(request,stu_id):
    if stu_id:

        try:
            stu_rem=Students.objects.get(id=stu_id)
            stu_rem.delete()
            return HttpResponse("students removed successfully")
        except:
             return HttpResponse('enter a valid student ')
        
    return render(request,'rem_stu.html')


def fil_Stu(request):
    if request.method == 'POST':
        name=request.POST.get('Name')
        cour=request.POST.get('cour')
        dur=request.POST.get('dur')
        stu=Students.objects.all()
        if name:
            stu=stu.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if cour:
            stu=stu.filter(cour_name=cour)
        if dur:
            stu=stu.filter(dur=dur)

        dict={
            "stu":stu
        }
        return render(request,'all_stu.html',dict)

    return render(request,'fil_stu.html')

