from django import template
from ..models import User

register = template.Library()


@register.filter(name='getUserFromId')
def getUserFromId(id):
    return User.objects.get(id=id)