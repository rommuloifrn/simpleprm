from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True)
    birthday = models.DateTimeField(auto_now_add=False, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    #relationship = models.ForeignKey("RelationshipType", null=True, verbose_name="Relationship Types", on_delete=models.SET_NULL)
    
    last_time_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    added = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class RelationshipType(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        app_label = 'core.relationship_type'