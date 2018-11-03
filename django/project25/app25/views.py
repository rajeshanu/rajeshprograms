from django.shortcuts import render
from .models import employee
from django.http import HttpResponse
import csv

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def showdetails(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    desig=request.POST.get("t3")
    salary=request.POST.get("t4")
    e1=employee(name=name,cno=cno,desig=desig,salary=salary)
    e1.save()
    return render(request,"index.html",{"message":"download details"})
def downdetails(request):
    http=HttpResponse(content_type='text/csv')
    http['content-Disposition']='attachment;filename="employee.csv"'
    w=csv.writer(http)
    e2=employee.objects.all()
    for x in e2:
        w.writerow([x.name,x.cno,x.desig,x.salary])
    return http