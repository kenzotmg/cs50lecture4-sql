from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.newlisting,name="newlisting"),
    path("listing/<int:id>", views.listing,name="listing"),
    path("addBid/<int:id>", views.addBid,name="addBid"),
    path("addToWatchList/<int:listingId>", views.addOrRemoveFromWatchList,name="addrmwatchlist"),
    path("watchlist", views.watchlist,name="watchlist"),
    path("closeauction/<int:listingId>", views.closeAuction, name="closeauction")
]
