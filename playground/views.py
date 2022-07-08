from django.shortcuts import render
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Order, OrderItem, Product, Customer
# Create your views here.

def say_hello(request):
    # select_related (1)
    # prefetch_related (2)
    # queryset = Customer.objects.annotate(
    #     #CONCAT
    #     full_name=Func(('first_name'),Value(' '), F('last_name'), function='CONCAT')
    # )
    # queryset = Customer.objects.annotate(
    #     #CONCAT
    #     full_name=Concat('first_name',Value(' '),'last_name')
    # )
    
    # return render(request, 'hello.html', {'name' : 'Mosh','result': list(queryset)})
    pass


