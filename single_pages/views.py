from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(
        request,
        'single_pages/Home.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
