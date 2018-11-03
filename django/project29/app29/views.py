from django.shortcuts import render
from .models import employee

# Create your views here.
def index(request):
    return render(request,"index.html")


def show(request):
    name = request.POST.get("name")
    cno = request.POST.get("age")
    desig = request.POST.get("desig")
    salary = request.POST.get("salary")
    e1 =employee(name=name, cno=cno, desig=desig, salary=salary)
    e1.save()
    return render(request, "index.html", {"message": "download details"})