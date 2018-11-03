from django.shortcuts import render


# Create your views here.
def showindex(request):
    return render(request,"index.html")


def show(request):
    key=request.POST.get("course")
    return render(request,"index.html",{"key":key})