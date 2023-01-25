from django.db import models

# Create your models here.


class Genre(models.Model):
    genre_name = models.CharField(max_length=255)


class Game(models.Model):
    game_image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    appid = models.IntegerField(null=True)
    game_name = models.CharField(max_length=255)
    release_date = models.DateField()
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genre = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.game_name

# for extracting ID's from 'Game' model JSON column that hold them.
class Genre_Extracted(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)













#ask chatgpt
#I created a new extracted table  with id as pk genre_id as fk for gamelist_genre and game_id as fk for gamelist_game
#I want game_id to have id's from gamelist_game and for genre_id to take from the JSON ARRAY column named genre in gamelist_game including all of the elements in each array  

