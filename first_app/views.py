from django.shortcuts import render
from first_app.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

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
    print("wefwe",request.user)
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse(index))

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

def search(request):
    if request.method == "GET":
        query = request.GET.get("q")
        restaurants = Restaurant.objects.filter(name__icontains = query)
        print(restaurants)
        return HttpResponse(restaurants[0].name)
