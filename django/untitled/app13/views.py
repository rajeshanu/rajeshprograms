from django.shortcuts import render
from app13.models import product
def showindex(request):
    p1=product.objects.all()
    return render(request,"index.html",{"product":p1})

def showregister(request):
    pno=request.POST.get("pno")
    pname=request.POST.get("pname")
    pprice=request.POST.get("pprice")
    pqty=request.POST.get("pqty")
    p=product(id=pno,name=pname,price=pprice,quntity=pqty)
    p.save()
    d1={"messege":"product data saved"}
    p1=product.objects.all()
    return render(request,"index.html",{"d1":d1,"product":p1})

def delete(request):
    id=request.POST.get("delete_id")
    print(id)
    product.objects.filter(id=id).delete()
    p1=product.objects.all()
    d2={"data modified"}
    return render(request,"index.html",{"d2":d2,"product":p1})

def update(request):
    id1=request.GET["update_id"]
    print(id1)
    p=product.objects.get(id=id1)
    p1=product.objects.all()
    return render(request,"index.html",{"product":p1,"p":p})
