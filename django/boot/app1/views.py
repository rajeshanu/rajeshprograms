from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def show(request):
    name=request.POST.get("email")
    password=request.POST.get("pass")


    if name=='rajeshanu414@gmail.com' and password=="rajesh":
        return render(request,"index.html",{"msg":"valid"})
    else:
        return render(request,"index.html",{"msg":"invalid"})