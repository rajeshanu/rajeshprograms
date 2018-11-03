from django.shortcuts import render
from django.http import HttpResponse
from app22.function import handle_uploaded_file
from app22.forms import StudentForm
def index(request):
    if request.method=='POST':
        student=StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded sucessfully")
    else:
        student=StudentForm()
        return render(request,"index.html",{"form":student})




