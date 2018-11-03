from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def show(request):
    name =request.POST.get("hero")
    print(name)
    return hero(request,name)
def hero(request,name):
    if name== 'pavan':
        list1=['kushi','balu','badri','tholiprema','thamudu']
        return render(request,"index.html",{"list":list1})
    elif name== 'Mahesh':
        list1=['okkadu','dookudu','pokiri','murari','one',]
        return render(request,"index.html",{"list":list1})
    elif name=='ntr':
        list1=['aadi','temper','jai lava kusha','aravinda sametha','janatha',]
        return render(request,"index.html",{"list":list1})
    else:
        return None
def movies(request):
    list=request.POST.getlist("movie")
    tli=tuple()
    for x in list:
        if x=='kushi':
            tli=tli+('kushi.jpg',)
        elif x=='badri':
            tli=tli+('badri.jpg',)
        elif x=='balu':
            tli=tli+('balu.jpg',)
        elif x=='tholiprema':
            tli=tli+('tholiprema.jpg',)
        elif x=='thamudu':
            tli=tli+('thamudu.jpg',)
        elif x=='okkadu':
            tli=tli+('okkadu.jpg',)
        elif x=='dookudu':
            tli=tli+('dookudu.jpg',)
        elif x=='pokiri':
            tli=tli+('pokiri.jpg',)
        elif x=='one':
            tli=tli+('one.jpg',)
        elif x=='murari':
            tli=tli+('murari.jpg',)
        elif x=='aadi':
            tli=tli+('aadi.jpg',)
        elif x=='temper':
            tli=tli+('temper.jpg',)
        elif x=='jai lava kusha':
            tli=tli+('jai.jpg',)
        elif x == 'aravinda sametha':
            tli = tli + ('aravinda.jpg',)
        elif x=='jantha':
            tli=tli+('janatha.jpg',)
    for x in tli:
        print(x)
    return render(request,"index.html",{"tli":tli})


