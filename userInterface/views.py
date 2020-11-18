from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'userInterface/index.html', context)

def careers(request):
    context = {}
    return render(request, 'userInterface/careers.html', context)

def aboutInfo(request):
    context = {}
    return render(request, 'userInterface/about-us.html', context)

def caseStudies(request):
    context = {}
    return render(request, 'userInterface/casestudies.html', context)

def inSights(request):
    context = {}
    return render(request, 'userInterface/eminsights.html', context)

def expertise(request):
    context = {}
    return render(request, 'userInterface/expertise.html', context)

def services(request):
    context = {}
    return render(request, 'userInterface/services.html', context)