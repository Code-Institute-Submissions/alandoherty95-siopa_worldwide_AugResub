from django.shortcuts import render
from products.models import Product
from django.db.models.functions import Lower


def show_favourites(request):
    """ View showing our favourite products in the store """
    products = Product.objects.filter(is_featured=True)
    sort = None
    direction = None
    # sorting favourites
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "color":
                sortkey = 'lower_color'
                products = products.annotate(lower_color=Lower("color"))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)
    # sorting directions 
    current_sorting = f'{sort}_{direction}'

    context = {
        'featured': products,
        'current_sorting': current_sorting,
    }

    return render(request, 'favourites/favourites.html', context)
