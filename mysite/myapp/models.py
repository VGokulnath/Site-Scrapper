from django.db import models

# Create your models here.

class Link(models.Model):

    def __str__ (self):
        return self.name if self.name else f"Link {self.id}"
    
    address = models.CharField(max_length=1000,null=True,blank=True)
    name = models.CharField(max_length=1000,null=True,blank=True)