from django.shortcuts import render
from django.http import HttpResponse
from app24.forms import profileform
from app24.models import profile
import os

def showindex(request):
    if request.method == 'POST':
        no = request.POST.get("sno")
        name = request.POST.get("name")
        cno = request.POST.get("cno")
        pro = profileform(request.POST, request.FILES)
        if pro.is_valid():
            if os.path.exists("app24/static/upload/" + cno):
                pass
            else:
                os.makedirs(r"app24/static/upload/" + cno)
            pf = request.FILES['file']

            with open('app24/static/upload/' + cno + '/' + pf.name, 'wb+') as d:
                for a in pf.chunks():
                    d.write(a)
            pr = profile.objects.last()
            p = 'upload/' + cno + '/' + pf.name
            p1 = profile.objects.last()
            id = 0
            if p1 == None:
                id += 1
            else:
                id = pr.no
                id = int(id) + 1
            d1 = profile(no=id, name=name, cno=cno, path=p)
            d1.save()
            d2 = profile.objects.all()
            return render(request, "index.html", {"form": pro, "d2": d2})
    else:
        emp = profileform()
        d2 =profile.objects.all()
    return render(request, "index.html", {"form": emp, "d2": d2})
