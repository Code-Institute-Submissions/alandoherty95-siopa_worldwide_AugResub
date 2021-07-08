from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is currently empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'sk_test_51JB136HDZWvoD6bS40LZkXT2v5pPQMZpWcFG15om5sr2x2dQRllzaQQc2RN6gyqH3lHODlcB5tQZAo1VJxaUzyu200gdKw0dvj',
        'client_secret': 'test secret key',
    }

    return render(request, template, context)
