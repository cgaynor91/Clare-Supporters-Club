from django.shortcuts import render

# Create your views here.
def index(request):
    """Displays index page"""
    return render(request, "index.html")