from django.shortcuts import render

# Create your views here.

def home(request):
    context = {"home_active": "active"}
    return render(request,"home.html", context)


def about(request):
    context = {"about_active": "active"}
    return render(request,"about.html", context)


def contact(request):
   context = {"contact_active": "active"}
   return render(request,"contact.html", context)


def services(request):
    context = {"services_active": "active"}
    return render(request,"services.html", context)