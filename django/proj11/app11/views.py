from django.shortcuts import render

def showindex(request):
    pno=request.POST.get("pno")
    pname=request.POST.get("pname")
    pprice=request.POST.get("pprice")
    pqty=request.POST.get("pqty")
    from  app11.models import product
    p1=product(id=pno,name=pname,price=pprice,quntity=pqty)
    p1.save()
    d1={"messege":"product data saved"}
    return render(request,"index.html",d1)
def showregister(request):
    return render(request,"index.html")

