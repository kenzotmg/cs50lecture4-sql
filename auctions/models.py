from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import URLValidator,MinValueValidator

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    starting_bid = models.IntegerField()
    picture = models.CharField(max_length=300,blank=True,default='https://cutt.ly/qvt7vz3')
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="products")
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=128)
    product = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="allcomments")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    
class Bid(models.Model):
    price = models.IntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name="allbids")
    bidder = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bids")

class Watchlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="watchedListings")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name="watchlist")