from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,'index.html')

d = {'nag':{'manam':"manam.jpg",'mass':'mass.jpg','manmadhudu':'manmadhudu.jpg'},
    'vijay':{'geetagovindam':'geetagovindam.jpg','arjunreddy':'arjunreddy.jpg','nota':'nota.jpg'},
    'uday':{'manasantanuvve':'manasantanuvve.jpg','neesneham':'neesneham.jpg','kalusukovalani':'kalusukovalani.jpg'}
         }

def showMovies(request):
    hero = request.POST.get('hero')
    res = d[hero]
    return render(request,'index.html',{'res':res,'hero':hero})


def displayPoster(request):
    hero = request.POST.get('he')
    mv_name = request.POST.getlist('movie')
    print(mv_name)
    mv_list = []
    for i in mv_name:
        mv_list.append(d[hero][i])
    res = d[hero]
    return render(request,'index.html',{'img_loc':mv_list,'res':res,'hero':hero})