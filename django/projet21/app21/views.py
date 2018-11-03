from django.shortcuts import render

h={
     "pavan":
                {
                "kushi":"kushi.jpg",
                "balu":"balu.jpg",
                "badri":"badri.jpg",
                "tholiprema":"tholiprema.jpg",
                "thamudu":"thamudu.jpg"
                 },
     "Mahesh":{
                "pokiri":"pokiri.jpg",
                "murari":"murari.jpg",
                "dookudu":"dookudu.jpg",
                "one":"one.jpg",
                "okkadu":"okkadu.jpg",
                },
      "ntr":{
              "aravinda sametha":"aravinda.jpg",
              "aadi":"aadi.jpg",
              "jailavakusha":"jai.jpg",
              "temper":"temper.jpg",
              "janatha":"janatha.jpg",
            },
 }

def showindex(request):
    return render(request,"index.html")
def show(request):
    hero = request.POST.get("hero")
    return render(request,"index.html",{"hero":h[hero],"hero1":hero})


def showmovie(request):
    image=request.POST.getlist("image")
    name=request.POST.get("name")
    res=h[name]
    list=[]
    for x in image:
        list=list+[h[name][x],]

    return render(request,"index.html",{"image":list,"hero":res,"h":h})
