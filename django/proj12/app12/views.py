from django.shortcuts import render
from app12.models import employee
# Create your views here.
def showindex(request):
    p1=employee.objects.all()
    p3=employee.objects.last()
    id2=0
    if p3==None:
        id=1
    else:
        id2=p3.id
        id2=(int(id2)+1)
    return render(request,"index.html",{"employee":p1,"key":id2})

def showregister(request):
    id=request.POST.get("idno")
    name=request.POST.get("name")
    salary=request.POST.get("salary")
    cno=request.POST.get("cno")
    p=employee(id=id,name=name,salary=salary,cno=cno)
    p.save()
    d1={"messege":"product data saved"}
    p1=employee.objects.all()
    p3 = employee.objects.last()
    id2 = 0
    if p3 == None:
        id = 1
    else:
        id2 = p3.id
        id2 = (int(id2))
    return render(request, "index.html", {"employee": p1, "key": id2})

def delete(request):
    id=request.POST.get("delete_id")
    print(id)
    employee.objects.filter(id=id).delete()
    p1=employee.objects.all()
    p3 = employee.objects.last()
    id2 = 0
    if p3 == None:
        id = 1
    else:
        id2 = p3.id
        id2 = (int(id2)+1)

    d2={"data modified"}
    return render(request,"index.html",{"d2":d2,"employee":p1,"key":id2})

def update(request):
    id1=request.GET["update_id"]
    p2=employee.objects.get(id=id1)
    return render(request,"update.html",{"p":p2,"id":id1})
def updatedetails(request):
    id1=request.GET["update_id"]
    id = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    cno = request.POST.get("cno")
    employee.objects.filter(id=id1).update(id=id,name=name,salary=salary,cno=cno)
    d3= {"messege": "product data update"}
    p1 = employee.objects.all()
    p3 = employee.objects.last()
    id2 = 0
    if p3 == None:
        id = 1
    else:
        id2 = p3.id
        id2 = (int(id2)+1)
    return render(request, "index.html", {"employee": p1, "key": id2})


