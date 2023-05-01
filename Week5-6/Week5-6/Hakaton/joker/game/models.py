from django.db import models

# Create your models here.
class Deck(models.Model):
    suit = models.CharField()
    value = models.CharField()
    color = models.CharField()
    
# class BigGame(models.Model):
#     big_game = models.IntegerField(blank=True, null=True)
#     distibution = models.IntegerField()
#     bet_p1 = models.IntegerField(blank=True, null=True)
#     bet_p2 = models.IntegerField(blank=True, null=True)
#     bet_p3 = models.IntegerField(blank=True, null=True)
#     bet_p4 = models.IntegerField(blank=True, null=True)
#     points1 = models.IntegerField(default=0)
#     points2 = models.IntegerField(default=0)
#     points3 = models.IntegerField(default=0)
#     points4 = models.IntegerField(default=0)
    
# class CurrentGame(models.Model):
#     step_num = models.CharField()
#     current_suit = models.CharField()
#     v1 = models.CharField()
#     s1 = models.CharField()
#     v2 = models.CharField()
#     s2 = models.CharField()
#     v3 = models.CharField()
#     s3 = models.CharField()
#     v4 = models.CharField()
#     s4 = models.CharField()
#     current_winner = models.CharField()


    