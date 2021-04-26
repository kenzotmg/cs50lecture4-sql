from django.contrib import admin
from .models import Bid,Comment,Listing,User,Watchlist

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id","title", "starting_bid", "picture", "description","active")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id","price", "listing_id", "bidder")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","comment")

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("user_id","listing_id")

# Register your models here.
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(User)
admin.site.register(Watchlist,WatchlistAdmin)