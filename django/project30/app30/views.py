from django.shortcuts import render
from .models import Feedback
def show(request):
    return render(request,"index.html")

def feedback(request):
    try:
        naa=request.session["status"]
        if naa:
            return render(request,"index.html",{"msg":"you have to give feedback for one time"})
        else:
            return render(request, "feedback.html")
    except KeyError:
        return render(request,"feedback.html")

def openfeedback(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    feedback=request.POST.get("t3")
    f=Feedback(name=name,cno=cno,feedback=feedback)
    f.save()
    request.session["status"]=True
    return render(request, "index.html",{"msg":"data saved"})