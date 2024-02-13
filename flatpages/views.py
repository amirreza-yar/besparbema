from django.shortcuts import render
# from django.views.decorators.cache import cache_page


def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def comming_soon(request, exception):
    return render(request, "comming-soon.html")