from django.contrib import admin
from .models import Bid,Comment,Listing,User

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id","title", "starting_bid", "picture", "description")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id","price", "listing_id", "bidder")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","comment")


# Register your models here.
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(User)