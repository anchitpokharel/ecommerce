from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView    
from rest_framework import status
from .models import *
from django.db.models.aggregates import Count
from .serializers import CollectionSerializer, ProductSerializer

# Create your views here.

class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
    
    # def get(self, request):
    #     queryset = Product.objects.select_related('collection').all()
    #     serializer = ProductSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     # print(serializer.validated_data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST'])
# def product_list(request): 
#     if request.method == 'GET':
        
    
#     elif request.method == 'POST':

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitems.count() > 0:
            return Response({'error':'Product cannot be deleted because it is associated with orderitem'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
# @api_view(['GET','PUT','DELETE']) 
# def product_detail(request, id):
    
#     if request.method == 'GET':
        
#     elif request.method == 'PUT': 
        
#     elif request.method == 'DELETE':
        

# @api_view(['GET','POST'])
# def collection_list(ListCreateAPIView): 
class CollectionList(ListCreateAPIView):  
    queryset =  Collection.objects.annotate(product_count = Count('products'))
    serializer_class = CollectionSerializer
    
    # if request.method == 'GET':
    #     collection = Collection.objects.annotate(product_count = Count('products'))
    #     serializer = CollectionSerializer(collection, many=True)
    #     return Response(serializer.data)
    
    # elif request.method == 'POST':
    #     serializer = CollectionSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.annotate(product_count = Count('products'))
    serializer_class = CollectionSerializer
    #lookup_field = 'id'
    
    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)        
        if collection.products.count() > 0:
                return Response({'error': 'Collection cannot be deleted as it is present in the products'})

        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET', 'PUT','DELETE'])
# def collection_detail(request, id):
#     collection = get_object_or_404(
#         Collection.objects.annotate(product_count = Count('products')),
#         pk=id
#     )
    
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
    
#     if request.method == 'PUT': 
#         serializer = CollectionSerializer(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         if collection.products.count() > 0:
#             return Response({'error': 'Collection cannot be deleted as it is present in the products'})
        
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)