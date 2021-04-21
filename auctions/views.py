from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.contrib import messages

from .models import User,Listing,Bid,Comment
from .forms.ListingForm import ListingForm
from .forms.CommentForm import CommentForm
from .forms.BidForm import BidForm


def index(request):
    return render(request, "auctions/index.html",{
        "listings" : Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='/login')
def newlisting(request):
    if request.method == "GET":
        return render(request, "auctions/newlisting.html", {
            "form" : ListingForm()
        })
    else:
        form = ListingForm(request.POST)
        if form.is_valid():
            # Check if user has provided an image and, if not, use default value
            if not form.cleaned_data['picture']:
                listing = Listing(title = form.cleaned_data['title'],starting_bid = form.cleaned_data['startingBid'],description = form.cleaned_data['description'],user = request.user)
                listing.save()
                return HttpResponseRedirect(reverse("index"))
            else:
                listing = Listing(title = form.cleaned_data['title'],starting_bid = form.cleaned_data['startingBid'],picture = form.cleaned_data['picture'],description = form.cleaned_data['description'],user = request.user)
                listing.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            populatedForm = ListingForm(request.POST)
            return render(request, "auctions/newlisting.html",{
                "form" : populatedForm
            })

def listing(request,id):
    if request.method == "GET":
        #Get listing by id
        listing = Listing.objects.get(id=id)
        user = User.objects.get(pk=listing.user_id)

        #Get all bids on listing
        oldBids = list(Bid.objects.filter(listing_id=id).order_by('-price').values())
        bid = listing.starting_bid
        if oldBids:
            bid = oldBids.pop(0)['price']  

        #Get comments on listing
        comments = listing.allcomments.all()

        commentForm = CommentForm(auto_id=False)

        #Create bid form
        bidForm = BidForm(minValue = bid)

        return render(request, 'auctions/listing.html',{
            "listing" : listing,
            "bid" : bid,
            "comments" : comments,
            "seller" : user,
            "id" : id,
            "commentForm" : commentForm,
            "oldBids" : oldBids,
            "bidForm" : bidForm
        })
    elif request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            product = Listing.objects.get(id=id)
            comment = Comment(comment = form.cleaned_data['comment'],product = product,user = request.user)
            comment.save()
            return HttpResponseRedirect(reverse('listing',kwargs={'id':id}))
        else:
            return render(request, "auctions/listing.html", {
                "commentForm" : form
            })

def addBid(request,id):
    if request.method == "GET":
        return render(request, 'auctions/index.html')
    elif request.method == "POST":
        maxBid = Bid.objects.filter(listing_id=id).order_by('-price').first().price
        if not maxBid:
            maxBid = Listing.objects.get(id=id)
            maxBid = maxBid.starting_bid
        form = BidForm(request.POST,minValue=maxBid)
        
        if form.is_valid():
            pass
        else:
            messages.warning(request,"Bid invalid!")
            return HttpResponseRedirect(reverse('listing',kwargs={'id':id}))