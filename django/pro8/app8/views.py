from django.shortcuts import render
from firebase import firebase as fab
fa = fab.FirebaseApplication("https://rajesh-fd194.firebaseio.com/Employee",None)
def showindex(request):
    return render(request,"index.html")
def showregister(request):
    id=request.GET.get("update_id")
    if id==None:
        d1= fa.get("Employee/", None)
        key=0
        if d1==None:
           key=101
        else:
            for x in d1:
             key=x
             key = int(key)+1
        return render(request,"register.html",{"key":key})
    else:
        d1 = fa.get("Employee/",id)
        return render(request,"register.html",{"key":id,"name": d1["name"], "cno": d1["cno"]})


def showviews(request):
        d2=fa.get("Employee/",None)
        return render(request,"views.html",{"d2":d2,"id":id})
def showdetails(request):
    id=request.POST["idno"]
    name=request.POST.get("uname")
    cno=request.POST.get("cno")

    d={"name":name,"cno":cno}
    fa.put("Employee/",id,d)
    return render(request,"index.html")
def deleteDetails(request):
    id = request.POST.get("delete_id")
    fa.delete("Employee/",id)
    return showviews(request)