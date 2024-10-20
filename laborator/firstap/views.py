from django.shortcuts import render
from .forms import UserForm
from django import forms
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        basket = request.POST.get("basket")
        email = request.POST.get("email")
        url_text = request.POST.get("url")
        file_path = request.FILES.get("file")
        regex = request.POST.get("regex")

        context = {
            'name': name,
            'age': age,
            'basket': basket,
            'email': email,
            'url_text': url_text,
            'file_path': file_path,
            'regex': regex
        }

        return render(request, "result.html", context)
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
def clock(request):
    return render(request, "clock.html")
def about (request):
    return HttpResponse("<h2>О сайте</h2>")
def contact (request):
    return HttpResponse("<h2>Контакты</h2>")
def products(request, productid=1):
    output="<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)
def users (request, id, name):
    output = "<h2>Пользователь</h2> <h3>ID: {0} Имя:{1}</h3>".format(id,name)
    return HttpResponse(output)