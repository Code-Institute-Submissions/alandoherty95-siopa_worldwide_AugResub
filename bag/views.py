from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product
# Create your views here.


def view_bag(request):
    """ VIEW SHOWING CONTENTS OF SHOPPING BAG """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ ALLOWS USERS TO ADD SPECIFIC PRODUCTS
    TO SHOPPING BAG INCLUDING QUANTITY OF ITEMS """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Successfully added {product.name} to shopping bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ ADJUSTS QUANTITY OF SPECIFIC ITEM """
  
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ REMOVES ITEM FROM SHOPPING BAG """

    bag = request.session.get('bag', {})
    bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
