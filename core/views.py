from django.shortcuts import render,redirect

def getDashboard(request):
    return render(request, 'Dashboard.html')

# Create your views here.
