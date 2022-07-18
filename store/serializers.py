import collections
from itertools import product
from pyexpat import model
from django.db.models.aggregates import Count
from rest_framework import serializers
from .models import *
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'id', 
            'title',
            'product_count',
        ]
    product_count = serializers.IntegerField(read_only=True)
    
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 
            'title',
            'description', 
            'slug', 
            'inventory',
            'unit_price',
            'price_with_tax',
            'collection'
        ]
    
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=9, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # # collection = CollectionSerializer()
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name = 'collection-detail',
    # )
    
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError("Passwords do not match")
    #     return data
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'name',
            'description'
        ]