from django.shortcuts import render
from app2.models import shop
def showindex(request):
    s1=shop.objects.all()
    return render(request,"index.html",{"shop":s1})

def showregister(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    price=request.POST.get("price")
    qty=request.POST.get("qty")
    s=shop(id=id,name=name,price=price,quntity=qty)
    s.save()
    d1={"messege":"product data saved"}
    s1=shop.objects.all()
    return render(request,"index.html",{"d1":d1,"shop":s1})

def delete(request):
    id=request.POST.get("delete_id")
    shop.objects.filter(id=id).delete()
    s1=shop.objects.all()
    d2={"data modified"}
    return render(request,"index.html",{"d2":d2,"shop":s1})

def update(request):
    id1=request.GET["update_id"]
    s=shop.objects.get(id=id1)
    s1=shop.objects.all()
    d3={"messege 2":"data update"}
    return render(request,"index.html",{"shop":s1,"s":s,"d3":d3})

