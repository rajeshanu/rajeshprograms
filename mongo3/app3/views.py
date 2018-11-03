from django.shortcuts import render
from .models import shop
# Create your views here.
def showindex(request):
    s1 = shop.objects.all()
    return render(request, "index.html", {"s1": s1})



def savedetails(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    salary=request.POST.get("salary")
    s=shop(id=id,name=name,salary=salary)
    s.save()
    s1=shop.objects.all()
    return render(request,"index.html",{"s1":s1})


def deleteitem(request):
    id1=request.POST.get("delete")
    shop.objects.filter(id=id1).delete()
    s1=shop.objects.all()
    return render(request,"index.html",{"s1":s1})


def updateitem(request):
    id2=request.GET["update"]
    s2=shop.objects.get(id=id2)
    s1=shop.objects.all()
    return render(request,"index.html",{"s1":s1,"s2":s2})