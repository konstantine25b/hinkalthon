from .models import Node, Data
from rest_framework import serializers

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'
        
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id','data' , 'creator_node']
        create_only_fields = ['data']
        read_only_fields = ['id']
        
class Ans(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['hash']
        