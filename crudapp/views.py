from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from crudapp.models import Student
# Create your views here.
def crud_opertions(request):
    if request.method=="GET":
        b=request.GET['b']
        if b=="Add":
            resp=insert_data(request)
            return resp
        elif b=="Update":
            resp=insert_data(request)
            return resp
        elif b=="Delete":
            resp=insert_data(request)
            return resp
        elif b=="Result":
            res=insert_data(request)
            return res
def insert_data(request):
    rno=request.GET.get("rno")
    s1=request.GET.get("sub1")
    s2=request.GET.get("sub2")
    stud=Student(rollno=rno,subject1=s1,subject2=s2)
    stud.save()
    msg={'msg':"maks are added"}
    r=render(request,"home.html",context=msg)
    return r
def result(request):
    rno=request.GET.get("rno")
    stud=Student.objects.get(rollno=rno)
    output=f'''<h2>Rollno{rno}<br>
       Subject1 {stud.subject1}<br>
       Subject2 {stud.subject2}<br>'''
    res="pass" if stud.subject1>=40 and stud.subject2>40 else "fail"
    output=output+"Result"+res
    return HttpResponse(output)
def home(request):
    r=render(request,"home.html")
    return r

