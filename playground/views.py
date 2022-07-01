from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from store.models import OrderItem, Product
# Create your views here.

def say_hello(request):
    # select_related (1)
    # prefetch_related (2)
    product = Product.objects.prefetch_related('promotions').all()
    return render(request, 'hello.html', {'title' : 'oooooooooooooooooooooooooooooooo', 'product': list(product)})
