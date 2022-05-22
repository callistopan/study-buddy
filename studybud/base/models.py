from django.db import models

# Create your models here.
class Room(models.Model):
    #host=
    #topic
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True) #it can be blank
    #participants=
    updated=models.DateTimeField(auto_now=True) #time when the room was updated
    created=models.DateTimeField(auto_now_add=True) #time when the room was created

    def __str__(self):
        return self.name




