from django.contrib import admin
from django.http import HttpRequest
from . import models
from django.db.models.aggregates import Count
# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_select_related = ['collection']
    
    def collection_title(self, product):
        return product.collection.title
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'

    ordering = ['inventory']
    list_editable = ['unit_price']



@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    #autocomplete_fields = ['featured_product']
    list_display = ['title', 'products_count']
    #search_fields = ['title']
    
    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
            )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']  
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'placed_at', 'payment_status', 'customer_name'
    ]
    list_select_related = ['customer']

    def customer_name(self, order):
        return order.customer.first_name + ' ' + order.customer.last_name

    ordering = ['customer__first_name', 'customer__last_name']
    list_editable = ['payment_status']