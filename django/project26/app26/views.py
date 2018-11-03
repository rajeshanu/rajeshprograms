from django.shortcuts import render
from django.http import HttpResponse
import csv
# Create your views here.
def showindex(request):
    return render(request,"index.html")


def showdetails(request):
    http=HttpResponse(content_type='text/csv')
    http['content-disposition']='attachment;filename="employee"'
    w=csv.writer(http)
    w.writerow(['101','raj',122000.00])
    w.writerow(['102','jay',185000.00])
    w.writerow(['103','sumanth',150000.00])
    w.writerow(['104','mahi',150000.00])
    return http