from rest_framework import generics 
from rest_framework.views import APIView
from .models import *
from .serializers import (
    NodeSerializer ,DataSerializer,Ans
)
import hashlib

class NodeListCreateView(generics.ListCreateAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    
    
class DataListCreateView(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    def perform_create(self, serializer):
        data = self.request.data.get('data')
        hash = hashlib.sha256(data.encode()).hexdigest()
        serializer.save(hash=hash, node = Node.objects.all())
    
         
    
class DataDetailView(generics.RetrieveAPIView):
    queryset = Data.objects.all()
    serializer_class = Ans
   
    



    
    
    