from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ VIEW SHOWING CONTENTS OF SHOPPING BAG """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ ALLOWS USERS TO ADD SPECIFIC PRODUCTS 
    TO SHOPPING BAG INCLUDING QUANTITY OF ITEMS """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)