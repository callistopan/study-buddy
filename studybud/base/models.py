from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A topic can have multiple rooms


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # it can be blank
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    # time when the room was updated
    updated = models.DateTimeField(auto_now=True)
    # time when the room was created
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.name

#One room can have multiple messages
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # room is the foreign key to the room model and cascade means if the room is deleted then the messages are deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    # time when the room was updated
    updated = models.DateTimeField(auto_now=True)
    # time when the room was created
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.body[:50]
