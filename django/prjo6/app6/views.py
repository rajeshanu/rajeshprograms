from django.shortcuts import render
def showindex(request):
    return render(request,"index.html")
