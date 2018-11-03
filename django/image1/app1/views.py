from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def showimage(request):
    name=request.POST.get("t1")
    if name=="pawan" or name=="ntr" or name=="mahesh":
      return render(request,"image.html",{"name":name})
    else:
        return render(request,"index.html",{"msg":"no image"})