from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def fashion(request):
    return render(request, 'fashion.html')

def food(request):
    return render(request, 'food.html')

def cinema(request):
    return render(request, 'cinema.html')

def contact(request):
    return render(request, 'contact.html')
