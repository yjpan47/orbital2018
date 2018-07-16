import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

from random import randint, choice
from datetime import *
from first_app.models import *
from faker import Faker

fakegen = Faker()

def populate_users(N = 1000):
    for i in range(N):
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_username = (fake_firstname + fake_lastname).lower() + str(randint(0, 100))
        fake_password = fakegen.password()
        fake_email = fakegen.email()
        fake_about_me = fakegen.text()
        fake_user = User(username = fake_username, first_name = fake_firstname, last_name = fake_lastname, email = fake_email)
        fake_user.set_password(fake_password)
        fake_user.save()
        fake_userprofile = UserProfile(user = fake_user, about_me = fake_about_me)
        fake_userprofile.save()

def populate_locations():
    lst = ["Techno Edge", "The Deck", "Frontier", "Pines Food Court", "Foodclique", "The Terrace", "Central Square", "Fine Food"]
    for i in lst:
        location = Location(location_name = i)
        location.save()

def populate_restaurants(N = 50):
    for i in range(N):
        fake_name = fakegen.last_name() + choice([" Stall", " Restaurant"])
        fake_location = choice(Location.objects.all())
        fake_address = fakegen.address()
        fake_information = fakegen.text()
        restaurant = Restaurant(name = fake_name, location = fake_location, address = fake_address, information = fake_information)
        restaurant.save()

def populate_openinghours():
    for r in Restaurant.objects.all():
        opening_hours = OpeningHours(
            restaurant = r,
            monday_from = time(hour = randint(6, 10)),
            monday_to = time(hour = randint(15, 19)),
            tuesday_from = time(hour = randint(6, 10)),
            tuesday_to = time(hour = randint(15, 19)),
            wednesday_from = time(hour = randint(6, 10)),
            wednesday_to = time(hour = randint(15, 19)),
            thursday_from = time(hour = randint(6, 10)),
            thursday_to = time(hour = randint(15, 19)),
            friday_from = time(hour = randint(6, 10)),
            friday_to = time(hour = randint(15, 19)),
            saturday_from = time(hour = randint(6, 10)),
            saturday_to = time(hour = randint(15, 19)),
            sunday_from = time(hour = randint(6, 10)),
            sunday_to = time(hour = randint(15, 19)), )
        opening_hours.save()

def populate_restaurant_ratings(N=100):
    for i in range(N):
        fake_rating = randint(0, 5)
        fake_restaurant = choice(Restaurant.objects.all())
        fake_user = choice(User.objects.all())
        restaurant_ratings = RestaurantRating(rating = fake_rating, restaurant = fake_restaurant, user = fake_user)
        restaurant_ratings.save()

def populate_restaurant_reviews(N=100):
    for i in range(N):
        fake_review = fakegen.text()
        fake_restaurant = choice(Restaurant.objects.all())
        fake_user = choice(User.objects.all())
        restaurant_review = ResturantReview(review = fake_review, restaurant = fake_restaurant, user = fake_user)
        restaurant_review.save()

def populate_restaurant_waiting_times(N=100):
    for i in range(N):
        fake_waiting_time = timedelta(minutes = randint(0, 20))
        fake_restaurant = choice(Restaurant.objects.all())
        fake_user = choice(User.objects.all())
        restaurant_waiting_time = RestaurantWaitingTime(waiting_time = fake_waiting_time, restaurant = fake_restaurant, user = fake_user)
        restaurant_waiting_time.save()

def populate_restaurant_crowd_conditions(N=100):
    for i in range(N):
        fake_crowd_conditon = randint(0, 10)
        fake_restaurant = choice(Restaurant.objects.all())
        fake_user = choice(User.objects.all())
        restaurant_crowd_condition = RestaurantCrowdCondition(crowd_condition = fake_crowd_conditon, restaurant = fake_restaurant, user = fake_user)
        restaurant_crowd_condition.save()

def populate_dishes(N=1000):
    for i in range(N):
        fake_name = fakegen.last_name() + choice([" Meal", " Dish"])
        fake_restaurant = choice(Restaurant.objects.all())
        fake_information = fakegen.text()
        dish = Dish(name = fake_name, restaurant = fake_restaurant, information = fake_information)
        dish.save()

def populate_dish_ratings(N=1000):
    for i in range(N):
        fake_rating = randint(0, 5)
        fake_dish = choice(Dish.objects.all())
        fake_user = choice(User.objects.all())
        dish_ratings = DishRating(rating = fake_rating, dish = fake_dish, user = fake_user)
        dish_ratings.save()

def populate_dish_reviews(N=1000):
    for i in range(N):
        fake_review = fakegen.text()
        fake_dish = choice(Dish.objects.all())
        fake_user = choice(User.objects.all())
        dish_review = DishReview(review = fake_review, dish = fake_dish, user = fake_user)
        dish_review.save()

if __name__ == '__main__':
    print("POPULATING DATABASE")
    populate_users(N = 200)
    print("1")
    populate_locations()
    print("2")
    populate_restaurants(N = 100)
    print("3")
    populate_openinghours()
    print("4")
    populate_restaurant_ratings(N = 200)
    print("5")
    populate_restaurant_reviews(N = 200)
    print("6")
    populate_restaurant_waiting_times(N = 200)
    print("7")
    populate_restaurant_crowd_conditions(N = 200)
    print("8")
    populate_dishes(N = 500)
    print("9")
    populate_dish_ratings(N = 300)
    print("10")
    populate_dish_reviews(N = 300)
    print("COMPLETE")
