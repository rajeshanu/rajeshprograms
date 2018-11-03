from django.shortcuts import render
import datetime
# Create your views here.
def showindex(request):
    date=datetime.datetime.now()
    crt_date=date.strftime("%y-%m-%d")
    max_date=date+datetime.timedelta(days=45)
    max_date=max_date.strftime("%y-%m-%d")
    return render(request,"index.html",{"current_date":crt_date,"max_date":max_date})


def show(request):
    dob=request.POST.get("dob")
    doj=request.POST.get("doj")
    date_period=request.POST.get("date_period")
    date=datetime.datetime.now()
    crt_date = date.strftime("%y-%m-%d")
    max_date = date + datetime.timedelta(days=45)
    max_date = max_date.strftime("%y-%m-%d")
    return render(request, "index.html", {"current_date": crt_date, "max_date": max_date,"dob":dob,"doj":doj,"date_period":date_period})