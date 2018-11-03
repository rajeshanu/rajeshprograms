from django.shortcuts import render
from django.http import HttpResponse
from app23.forms import EmployeeForm
import os
from app23.models import Employee



def showindex(request):
    if request.method == 'POST':
        sno=request.POST.get("sno")
        name=request.POST.get("name")
        cno=request.POST.get("cno")
        emp = EmployeeForm(request.POST, request.FILES)
        if emp.is_valid():
            if os.path.exists("app23/static/upload/"+cno):
                pass
            else:
                os.makedirs(r"app23/static/upload/"+cno)
            se=request.FILES['file']

            with open('app23/static/upload/'+cno+'/'+se.name,'wb+') as d:
                for a in se.chunks():
                    d.write(a)
            e=Employee.objects.last()
            p='upload/'+cno+'/'+se.name
            p1=Employee.objects.last()
            id=0
            if p1==None:
                id+=1
            else:
                id=e.sno
                id=int(id)+1
            d1=Employee(sno=id,name=name,cno=cno,path=p)
            d1.save()
            d2=Employee.objects.all()
            return render(request,"index.html",{"form":emp,"d2":d2})
    else:
        emp=EmployeeForm()
        d2 = Employee.objects.all()
    return render(request,"index.html",{"form":emp,"d2":d2})


