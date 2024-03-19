from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import student
from django.http import Http404
from django.contrib import auth

def home():
    return HttpResponse("Home page")

def hiname(username):
    return HttpResponse("Hi " + username)

def age(year):
    return HttpResponse("Age: " + str(year))

def hello_view(request):
    fourSeason = range(1, 5)
    p1 = {"name": "Amy", "phone": "0912-345678", "age": 20}
    p2 = {"name": "Jack", "phone": "0937-123456", "age": 25}
    p3 = {"name": "Nacy", "phone": "0958-654321", "age": 17}
    persons = [p1, p2, p3]
    return render(request, 'hello_django.html', {
        'title': "樣板使用",
        'data': "Hello Django!",
        'seasons': fourSeason,
        'persons': persons,
        'now': datetime.now()
    })

def getOneByName(request, username):
    title = "顯示一筆資料"
    try:
        unit = student.objects.get(cName=username)
    except student.DoesNotExist:
        raise Http404("查無此學生")
    except Exception as e:
        raise e
    return render(request, 'listone.html', locals())

def getAll(request):
    title = "顯示全部資料"
    try:
        students = student.objects.all()
    except student.DoesNotExist:
        raise Http404("查無學生資料")
    except Exception as e:
        raise e
    context = {
        'title': title,
        'students': students,
    }
    return render(request, 'listall.html', context)

def main(request):
    pageTitle="子網頁繼承"
    mainTitle="段落標題"
    mainContent="段落內文"
    artitle1={"aTitle":"文章標題","aContent":"文章1內文"}
    artitle2={"aTitle":"文章標題","aContent":"文章2內文"}
    artitles=[artitle1, artitle2]
    return render(request, 'index.html', locals())

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        uName = request.POST.get('uName')
        uPass = request.POST.get('uPass')
        
        user = auth.authenticate(username=uName, password=uPass)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("已登入")
        else:
            return redirect('/login/')
