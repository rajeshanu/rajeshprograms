from django.shortcuts import render

hero={
    "pawan":
    {
        "image":"kushi.jpg",
        "song":"pawan.mp3",

    },
    "ntr":
        {
            "image": "janatha.jpg",
            "song": "ntr.mp3",

        },
    "mahesh":
        {
            "image": "pokiri.jpg",
            "song": "mahesh.mp3",

        },

}
def showindex(request):
    return render(request,"index.html")


def pawan(request):
    p=request.POST.get("t1").lower()
    img=hero[p]
    return render(request,"image.html",{"img":img})
def ntr(request):
    p=request.POST.get("t1").lower()
    img=hero[p]
    return render(request,"image.html",{"img":img})
def mahesh(request):
    p=request.POST.get("t1").lower()
    img=hero[p]
    return render(request,"image.html",{"img":img})
def heros(request):
    hero=request.POST.get("t4").lower()
    res=hero[hero]
    return render(request,"image.html",{"res":res})