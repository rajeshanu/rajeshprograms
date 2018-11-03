from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def show(request):
    res = HttpResponse(content_type='application/pdf')
    res['Content-Disposition'] = 'attachment;filename = "somefilename.pdf"'
    p=canvas.Canvas(res)
    p.drawString(100, 100, "")
    p.showPage()
    p.save()
    return res