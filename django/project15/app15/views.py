from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def show(request):
    res=request.POST.get("date")
    print(res)
    return render(request,"index.html",{"res":res})