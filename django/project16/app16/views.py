from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")