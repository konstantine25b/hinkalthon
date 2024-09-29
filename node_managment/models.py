from django.db import models

# Create your models here.

class Node(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.title
    

class Data(models.Model):
    hash = models.TextField(blank=False, unique=True)
    data = models.TextField(blank=False)
    node = models.ManyToManyField(Node)
    creator_node = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.hash
   