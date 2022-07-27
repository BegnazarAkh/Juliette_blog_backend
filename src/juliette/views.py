from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def listing1(request):
    return render(request, 'listing-1.html', {})

def listing2(request):
    return render(request, 'listing-2.html', {})

def post(request):
    return render(request, 'post.html', {})
