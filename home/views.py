from django.shortcuts import render

# Create your views here.


def index(request):
    ''' VIEW RETURNING THE INDEX PAGE '''

    return render(request, 'home/index.html')
