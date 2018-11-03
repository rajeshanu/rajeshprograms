from django.shortcuts import render

def showindex(request):
    return render(request,"index.html")
def savedetails(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    cno= request.POST.get("cno")
    from app11.models import Employee
    d1 = Employee(id=id, name=name, salary=salary,cno=cno )
    d1.save()
    d1 = {"messege": "product data saved"}
    return render(request, "index.html", d1)

