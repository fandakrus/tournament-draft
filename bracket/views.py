from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request, 'bracket/index.html')


