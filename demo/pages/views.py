from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {}) 


def contact_view(*agrs, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")


def hello_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello "+str(request.user)+"</h1>") 

def show_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context= {
        'name': 'Shivam Agrawal',
        'city': 'Pipariya',
        'places': ['Manali', 'Kashmir', 'Peris', 'Nepal', 'World'],
        'age': 22,
        'headd': '<h2>Mumbai</h2>'
    }
    return render(request, 'about.html', my_context)