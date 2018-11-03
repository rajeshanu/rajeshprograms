from django.shortcuts import render
from .models import register
from app31.models import login

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def show(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    email=request.POST.get("t3")
    password=request.POST.get("t4")
    r=register(name=name,cno=cno,email=email,password=password)
    r.save()
    return render(request,"index.html",{"msg":"data saved"})


def login(request):
    email=request.POST.get("t5")
    password=request.POST.get("t6")
    #p=register(email=email,password=password)
    #p.save()
    s=register.objects.get(email=email)
    if s.email==email and s.password==password:
        return render(request,"details.html",{"email":s.email})
    else:
         return render(request,"index.html",{"msg2":"invalid"})

def profile(request):
    email=request.GET.get("email")
    d=register.objects.get(email=email)
    return render(request,"profile.html",{"email":email})
def feedback(request):
    uemail=request.GET.get("email")
    try:
        fmail=request.session["email"]
        if uemail==fmail:
          return render(request,"details.html",{"msg1":" already given feedback"})
        else:
            return render(request,"feedback.html",{"email":uemail})
    except:
        return render(request,"feedback.html",{"email":uemail})
def savefeedback(request):
    email=request.POST.get("id")
    feed=request.POST.get("msg")
    l=login(feedback=feed,uemail=email)
    l.save()
    request.session["email"]=email
    return render(request,"details.html",{"msg":"feedback given "})