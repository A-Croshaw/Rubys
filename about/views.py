import os
from django.shortcuts import render


def about(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')

def contact(request):
    """ A view to return the contact page """

    return render(request, 'about/contact.html', context={
        'EMAILJS': os.environ.get('EMAILJS')
    })