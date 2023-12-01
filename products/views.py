from django.shortcuts import get_object_or_404, redirect, render
from .models import Product

def all_products(request):
    """ A view to show all products, includes sorting and searches """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_view(request, product_id):
    """ View to see full product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_view.html', context)