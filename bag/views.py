from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ VIEW SHOWING CONTENTS OF SHOPPING BAG """

    return render(request, 'bag/bag.html')
