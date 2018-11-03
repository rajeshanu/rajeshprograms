from django.shortcuts import render


def showindex(request):
    return render(request,"index.html")


def show(request):
    check=request.POST.getlist("course")

    return render(request,"index.html",{"check":check})