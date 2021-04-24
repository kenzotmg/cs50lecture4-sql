from django import template
from ..models import User
from ..models import Listing
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter(name='getUserFromId')
def getUserFromId(id):
    return User.objects.get(id=id)

@register.filter(name='getWatchStateFromListing')
def getStateFromListing(listing,user_id):
    try:
        watchlist = listing.watchlist.get(user_id=user_id)
        return True
    except ObjectDoesNotExist:
        return False