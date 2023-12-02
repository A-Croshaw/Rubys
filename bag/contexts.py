from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def shopping_content(request):

    items_in_bag = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            items_in_bag.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                items_in_bag.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
        
                })
    if total > 0:
        if total < settings.FREE_DELIVERY:
        
            delivery = total + Decimal(settings.STANDARD_DELIVERY)
            free_delivery_difference = settings.FREE_DELIVERY - total
            
        else:
            delivery = 0
            free_delivery_difference= 0

    
    overal_total = delivery + total
    
    context = {
        'items_in_bag': items_in_bag,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_difference': free_delivery_difference,
        'free_delivery': settings.FREE_DELIVERY,
        'overal_total': overal_total,
    }

    return context