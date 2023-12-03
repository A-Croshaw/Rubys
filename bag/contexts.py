from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def shopping_content(request):

    items_in_cart = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})
    delivery = 0
    
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        if product.condtion == "used":
            price_used = product.price / 2
            total += quantity * price_used
            item_count += quantity

            items_in_cart.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        else:
            total += quantity * product.price
            item_count += quantity
            items_in_cart.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        
    if total >0:
         delivery = settings.STANDARD_DELIVERY
    if total < settings.FREE_DELIVERY:
        free_delivery_difference = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        free_delivery_difference = 0
    
    overal_total = delivery + total
    
    context = {
        'items_in_cart': items_in_cart,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_difference': free_delivery_difference,
        'free_delivery': settings.FREE_DELIVERY,
        'overal_total': overal_total,
    }

    return context