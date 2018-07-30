from django.shortcuts import render
from first_app.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def user_signup(request):

    registered = False

    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        year = request.POST.get("year")
        faculty = request.POST.get("faculty")
        course = request.POST.get("course")
        password = request.POST.get("password")
        about_me = request.POST.get("about_me")
        profile_pic = request.FILES.get("profile_pic")

        if username in list(map(lambda x: x.username, User.objects.all())):
            return render(request, 'first_app/signup_username_taken.html')

        user = User(username = username, first_name = first_name, last_name = last_name, email = email)
        user.set_password(password)
        user.full_clean()
        user.save()

        user_profile = UserProfile(user = user, year = year, faculty = faculty, course = course, about_me = about_me, profile_pic = profile_pic)
        user_profile.full_clean()
        user_profile.save()

        registered = True

        return render(request, 'first_app/signup_success.html')

    return render(request, 'first_app/signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)

        remember_me = request.POST.get("remember_me")

        if user:
            if remember_me == None:
                request.session.set_expiry(300)
            login(request, user)
            return render(request, 'first_app/login_success.html')
        else:
            return render(request, 'first_app/login_fail.html')
    else:
        return render(request, 'first_app/login.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("index")

def user_profile(request, pk):
    user = request.user
    profile_user = get_object_or_404(User, id = pk)
    return render(request, "first_app/profile.html", {"user": user, "profile_user": profile_user})

def edit_restaurant_review(request, pk):
    if request.user.is_authenticated:
        restaurant_review = get_object_or_404(RestaurantReview, id = pk)
        if restaurant_review in request.user.restaurantreview_set.all():
            if request.method == "POST":
                restaurant_review.review = request.POST.get("new_restaurant_review")
                restaurant_review.save()
                return redirect("profile", pk = request.user.id)
            else:
                return render(request, "first_app/edit_restaurant_review.html", {"restaurant_review": restaurant_review})
        else:
            return HttpResponse("FAILED")
    else:
            return HttpResponse("FAILED")

def delete_restaurant_review(request, pk):
    if request.user.is_authenticated:
        restaurant_review = get_object_or_404(RestaurantReview, id = pk)
        if restaurant_review in request.user.restaurantreview_set.all():
            if request.method == "POST":
                restaurant_review.delete()
                return redirect("profile", pk = request.user.id)
            else:
                return render(request, "first_app/delete_restaurant_review.html", {"restaurant_review": restaurant_review})
        else:
            return HttpResponse("FAILED")
    else:
            return HttpResponse("FAILED")

def edit_dish_review(request, pk):
    if request.user.is_authenticated:
        dish_review = get_object_or_404(DishReview, id = pk)
        if dish_review in request.user.dishreview_set.all():
            if request.method == "POST":
                dish_review.review = request.POST.get("new_dish_review")
                dish_review.save()
                return redirect("profile", pk = request.user.id)
            else:
                return render(request, "first_app/edit_dish_review.html", {"dish_review": dish_review})
        else:
            return HttpResponse("FAILED")
    else:
            return HttpResponse("FAILED")

def delete_dish_review(request, pk):
    if request.user.is_authenticated:
        dish_review = get_object_or_404(DishReview, id = pk)
        if dish_review in request.user.dishreview_set.all():
            if request.method == "POST":
                dish_review.delete()
                return redirect("profile", pk = request.user.id)
            else:
                return render(request, "first_app/delete_dish_review.html", {"dish_review": dish_review})
        else:
            return HttpResponse("FAILED")
    else:
            return HttpResponse("FAILED")

def delete_restaurant_photo(request, pk):
    if request.user.is_authenticated:
        restaurant_photo = get_object_or_404(RestaurantPhoto, id = pk)
        if restaurant_photo in request.user.restaurantphoto_set.all():
            if request.method == "POST":
                restaurant_photo.delete()
                return redirect("profile", pk = request.user.id)
            else:
                return render(request, "first_app/delete_restaurant_photo.html", {"restaurant_photo": restaurant_photo})
        else:
            return HttpResponse("FAILED")
    else:
            return HttpResponse("FAILED")

def add_restaurant_photo(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        restaurant = get_object_or_404(Restaurant, id = pk)
        photo = request.FILES.get("restaurant_photo")
        print("HELLO", photo == None)
        restaurant_photo = RestaurantPhoto(photo = photo, restaurant = restaurant, user = request.user)
        restaurant_photo.save()
        return redirect("restaurant", pk = restaurant.id)
    else:
        return HttpResponse("FAILED")

def restaurant_page(request, pk):
    restaurant = get_object_or_404(Restaurant, id = pk)
    return render(request, "first_app/restaurant.html", {"restaurant": restaurant})

def add_restaurant_rating(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        restaurant = get_object_or_404(Restaurant, id = pk)
        if request.user not in list(map(lambda obj: obj.user, restaurant.restaurantrating_set.all())):
            new_restaurant_rating = RestaurantRating(rating = int(request.POST.get("restaurant_rating")), restaurant = restaurant, user = request.user)
            new_restaurant_rating.save()
            return redirect("restaurant", pk = pk)
        else:
            return HttpResponse("You already contributed a rating")
    else:
        return HttpResponse("Something went wrong")

def add_restaurant_review(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        restaurant = get_object_or_404(Restaurant, id = pk)
        if request.user not in list(map(lambda obj: obj.user, restaurant.restaurantreview_set.all())):
            new_review = RestaurantReview(review = request.POST.get("restaurant_review"), restaurant = restaurant, user = request.user)
            new_review.save()
            return redirect("restaurant", pk = pk)
        else:
            return HttpResponse("You contributed a review already")
    else:
        return HttpResponse("Something went wrong")

def add_restaurant_waiting_time(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        restaurant = get_object_or_404(Restaurant, id = pk)
        if request.user not in list(map(lambda obj: obj.user, restaurant.get_waiting_time_objects())):
            new_waiting_time = RestaurantWaitingTime(waiting_time = int(request.POST.get("waiting_time")), restaurant = restaurant, user = request.user)
            new_waiting_time.save()
            return redirect("restaurant", pk = pk)
        else:
            return HttpResponse("You contributed a waiting time already")
    else:
        return HttpResponse("Something went wrong")

def add_restaurant_crowd_condition(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        restaurant = get_object_or_404(Restaurant, id = pk)
        if request.user not in list(map(lambda obj: obj.user, restaurant.get_crowd_condition_objects())):
            new_crowd_condition = RestaurantCrowdCondition(crowd_condition = int(request.POST.get("crowd_condition")), restaurant = restaurant, user = request.user)
            new_crowd_condition.save()
            return redirect("restaurant", pk = pk)
        else:
            return HttpResponse("You contributed a crowd condition already")
    else:
        return HttpResponse("Something went wrong")

def add_restaurant_review_rating(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        restaurant_review = get_object_or_404(RestaurantReview, id = pk)
        if request.user not in list(map(lambda obj: obj.user, restaurant_review.restaurantreviewrating_set.all())):
            restaurant = restaurant_review.restaurant
            new_restaurant_review_rating = RestaurantReviewRating(rating = int(request.POST.get("restaurant_review_rating")), restaurant_review = restaurant_review, user = request.user)
            new_restaurant_review_rating.save()
            return HttpResponseRedirect(request.POST.get('next'))
        else:
            return HttpResponse("You already contributed a rating")
    else:
        return HttpResponse("Something went wrong")

def add_dish_review_rating(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        dish_review = get_object_or_404(DishReview, id = pk)
        if request.user not in list(map(lambda obj: obj.user, dish_review.dishreviewrating_set.all())):
            dish = dish_review.dish
            new_dish_review_rating = DishReviewRating(rating = int(request.POST.get("dish_review_rating")), dish_review = dish_review, user = request.user)
            new_dish_review_rating.save()
            return HttpResponseRedirect(request.POST.get('next'))
        else:
            return HttpResponse("You already contributed a rating")
    else:
        return HttpResponse("Something went wrong")

def dish_page(request, pk):
    dish = get_object_or_404(Dish, id = pk)
    print("Test", dish)
    return render(request, "first_app/dish.html", {"dish": dish})

def add_dish_rating(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        dish = get_object_or_404(Dish, id = pk)
        if request.user not in list(map(lambda obj: obj.user, dish.dishrating_set.all())):
            new_dish_rating = DishRating(rating = int(request.POST.get("dish_rating")), dish = dish, user = request.user)
            new_dish_rating.save()
            return HttpResponseRedirect(request.POST.get('next'))
        else:
            return HttpResponse("You already contributed a rating")
    else:
        return HttpResponse("Something went wrong")

def add_dish_review(request, pk):
    if (request.method == "POST") and (request.user.is_authenticated):
        dish = get_object_or_404(Dish, id = pk)
        if request.user not in list(map(lambda obj: obj.user, dish.dishreview_set.all())):
            new_dish = DishReview(review = request.POST.get("dish_review"), dish = dish, user = request.user)
            new_dish.save()
            return HttpResponseRedirect(request.POST.get('next'))
        else:
            return HttpResponse("You contributed a review already")
    else:
        return HttpResponse("Something went wrong")

def search(request):
    if "q" in request.GET:
        sort_by = request.GET.get('sort', "name")
        location_filter = request.GET.get('location')
        page = request.GET.get('page', 1)
        query = request.GET.get("q")
        restaurants = list(Restaurant.objects.filter(name__icontains = query).order_by("name"))

        if sort_by == "ratings":
            restaurants.sort(key = lambda obj: obj.get_average_rating(), reverse = True)
        if sort_by == "crowd":
            restaurants.sort(key = lambda obj: obj.get_crowd_condition(), reverse = False)

        if location_filter:
            restaurants = list(filter(lambda obj: obj.location == location_filter, restaurants))

        paginator = Paginator(restaurants, 10)
        restaurants = paginator.page(page)
        return render(request, "first_app/search.html", {"restaurants": restaurants, "q": query})
    else:
        return HttpResponse("Something went wrong")
