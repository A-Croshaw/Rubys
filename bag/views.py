from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def shopping_cart(request):
    """ View that renders the shopping cart """

    return render(request, 'bag/cart.html')

def cart_add(request, item_id):
    """ Adding products to shopping cart with quantities"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
         cart[item_id] += quantity
         messages.success(request, f'Added {product.title} to {cart[item_id]}')
    else:
         cart[item_id] = quantity
         messages.success(request, f'Added {product.title} to {cart[item_id]}')
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def cart_update(request, item_id):
    """Adjust the quantity"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.title} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.title} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def item_remove(request, item_id):
    """Remove items from cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {product.title} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)