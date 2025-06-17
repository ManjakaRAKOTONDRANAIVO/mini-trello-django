from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class List(models.Model):
    name = models.CharField(max_length=225)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="list")
    position = models.IntegerField(default=0) # pour l'ordre des listes
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="cards")
    position = models.IntegerField(default=0)  # pour l'ordre des cartes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title