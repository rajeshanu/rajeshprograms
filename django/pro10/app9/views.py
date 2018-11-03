from django.shortcuts import render
from firebase import firebase as fab
fa= fab.FirebaseApplication("https://raju-45416.firebaseio.com/Employee",None)
def showindex(request):
    return render(request,"index.html")
def showregister(request):
    id=request.GET.get("update_id")
    if id==None:
        key = 0
        d2 = fa.get("Employee/", None)
        if d2 == None:
            key = 101
        else:
            for x in d2:
                key = x
        key = int(key) + 1
        return render(request,"register.html",{"key":key})
    else:
        d2=fa.get("Employee/",id)
        return render(request,"register.html",{"key":id,"name":d2["name"],"cno":d2["cno"]})
def showview(request):
    d3=fa.get("Employee/",None)
    return render(request,"views.html",{"d3":d3})

def showdetails(request):
    id=request.POST["idno"]
    name=request.POST.get("name")
    cno=request.POST.get("cno")
    d1={"name":name,"cno":cno,"id":id}
    fa.put("Employee/",id,d1)
    return render(request,"index.html")

def deletedetails(request):
    id = request.POST.get("delete")
    fa.delete("Employee/", id)
    return showview(request)
