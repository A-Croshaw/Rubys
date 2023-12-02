from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def shopping_bag(request):
    """ View that renders the shopping bag """

    return render(request, 'bag/bag.html')

def bag_add(request, item_id):
    """ Adding products to shopping bag with quantities"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
         bag[item_id] += quantity
    else:
         bag[item_id] = quantity
    
    request.session['bag'] = bag
    return redirect(redirect_url)