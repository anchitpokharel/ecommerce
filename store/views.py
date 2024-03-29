from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet    
from rest_framework import status
from .models import *
from django.db.models.aggregates import Count
from .serializers import *

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error':'Product cannot be deleted because it is associated with orderitem'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class CollectionViewSet(ModelViewSet):
    queryset =  Collection.objects.annotate(product_count = Count('products'))
    serializer_class = CollectionSerializer


    def destroy(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)        
        if collection.products.count() > 0:
                return Response({'error': 'Collection cannot be deleted as it is present in the products'})

        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer