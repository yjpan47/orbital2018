from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import localtime
from datetime import timedelta

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='userprofile')
    # Additional
    year = models.CharField(max_length = 10, blank = True)
    faculty = models.CharField(max_length = 256, blank = True)
    course = models.CharField(max_length = 256, blank = True)
    about_me = models.TextField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)
    def __str__(self):
        return self.user.username

class Location(models.Model):
    location_name =  models.CharField(max_length = 264, unique = True)
    def __str__(self):
        return self.location_name

class Restaurant(models.Model):
    name = models.CharField(max_length = 256)
    restaurant_profile_pic = models.ImageField(upload_to = 'restaurant_profile_pics', blank = True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    address = models.CharField(max_length=256)
    information = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_restaurant_reviews(self):
        reviews_list = list(self.restaurantreview_set.all())
        reviews_list.sort(key = lambda obj: obj.get_average_rating(), reverse = True)
        return reviews_list

    def get_restaurant_reviews_most_recent(self):
        reviews_list = list(self.restaurantreview_set.all())
        reviews_list.sort(key = lambda obj: obj.created_at, reverse = True)
        return reviews_list

    def get_restaurant_photos(self):
        photos_list = list(self.restaurantphoto_set.all())
        photos_list.sort(key = lambda obj: obj.created_at, reverse = True)
        return photos_list

    def get_restaurant_reviews(self):
        reviews_list = list(self.restaurantreview_set.all())
        reviews_list.sort(key = lambda obj: obj.get_average_rating(), reverse = True)
        return reviews_list

    def number_of_reviews(self):
        return len(self.restaurantreview_set.all())

    def get_average_rating(self):
        lst = list(map(lambda x: x.rating, (self.restaurantrating_set.all())))
        return round(sum(lst)/len(lst), 1) if lst else 0

    def get_waiting_time_objects(self, mins = 10):
        start, end = localtime() - timedelta(seconds = mins), localtime()
        return list(filter(lambda obj: start < localtime(obj.created_at) < end, self.restaurantwaitingtime_set.all()))

    def get_waiting_time(self, mins = 30):
        start, end = localtime() - timedelta(seconds = mins), localtime()
        lst = list(filter(lambda obj: start < localtime(obj.created_at) < end, self.restaurantwaitingtime_set.all()))
        return round(sum(list(map(lambda obj: obj.waiting_time, lst)))/len(lst), 2) if len(lst) else ""

    def get_crowd_condition_objects(self, mins = 10):
        start, end = localtime() - timedelta(seconds = mins), localtime()
        return list(filter(lambda obj: start < localtime(obj.created_at) < end, self.restaurantcrowdcondition_set.all()))

    def get_crowd_condition(self, mins = 30):
        start, end = localtime() - timedelta(seconds = mins), localtime()
        lst = list(filter(lambda obj: start < localtime(obj.created_at) < end, self.restaurantcrowdcondition_set.all()))
        int_result = int(round(sum(list(map(lambda obj: obj.crowd_condition, lst)))/len(lst), 0)) if len(lst) else ""
        if int_result == 1: return "Not Busy"
        elif int_result == 2: return "Fairly Busy"
        elif int_result == 3: return "Very Busy"
        else: return ""

    def highest_rated_dish(self):
        dishes_list = list(self.dish_set.all())
        dishes_list.sort(key = lambda obj: obj.get_average_rating(), reverse = True)
        if dishes_list:
            return dishes_list[0]

    def get_opening_hours_today(self):
        if localtime().weekday() == 0:
            return (self.openinghours.monday_from.strftime("%H:%M"), self.openinghours.monday_to.strftime("%H:%M"))
        if localtime().weekday() == 1:
            return (self.openinghours.tuesday_from.strftime("%H:%M"), self.openinghours.tuesday_to.strftime("%H:%M"))
        elif localtime().weekday() == 2:
            return (self.openinghours.wednesday_from.strftime("%H:%M"), self.openinghours.wednesday_to.strftime("%H:%M"))
        elif localtime().weekday() == 3:
            return (self.openinghours.thursday_from.strftime("%H:%M"), self.openinghours.thursday_to.strftime("%H:%M"))
        elif localtime().weekday() == 4:
            return (self.openinghours.friday_from.strftime("%H:%M"), self.openinghours.friday_to.strftime("%H:%M"))
        elif localtime().weekday() == 5:
            return (self.openinghours.saturday_from.strftime("%H:%M"), self.openinghours.saturday_to.strftime("%H:%M"))
        elif localtime().weekday() == 6:
            return (self.openinghours.sunday_from.strftime("%H:%M"), self.openinghours.sunday_to.strftime("%H:%M"))

    def get_weekday(self):
        return localtime().weekday()

    def is_open(self):
        start, end = self.get_opening_hours_today()
        if start < localtime().strftime("%H:%M") < end:
            return True
        else:
            return False

    def get_verified_dishes(self):
        dishes = list(self.dish_set.all())
        dishes = list(filter(lambda obj: obj.verified == True, dishes))
        print(dishes[-1].verified)
        return dishes

class OpeningHours(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete = models.CASCADE)
    monday_from = models.TimeField()
    monday_to = models.TimeField()
    tuesday_from = models.TimeField()
    tuesday_to = models.TimeField()
    wednesday_from = models.TimeField()
    wednesday_to = models.TimeField()
    thursday_from = models.TimeField()
    thursday_to = models.TimeField()
    friday_from = models.TimeField()
    friday_to = models.TimeField()
    saturday_from = models.TimeField()
    saturday_to = models.TimeField()
    sunday_from = models.TimeField()
    sunday_to = models.TimeField()

    def __str__(self):
        return "Opening Hours: {}".format(self.restaurant)

class RestaurantRating(models.Model):
    rating = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Restaurant Rating: {}, {}, {}".format(self.user, self.restaurant, self.rating)

class RestaurantReview(models.Model):
    review = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Restaurant Review: {}, {}".format(self.user, self.restaurant)

    def get_average_rating(self):
        lst = list(map(lambda x: x.rating, (self.restaurantreviewrating_set.all())))
        return round(sum(lst)/len(lst), 1) if lst else 0

    def get_time(self):
        return localtime(self.created_at).strftime("%d %B %Y, %H:%M")

class RestaurantReviewRating(models.Model):
    rating = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    restaurant_review = models.ForeignKey(RestaurantReview, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Restaurant Review Rating: {}, {}".format(self.user, self.restaurant_review)

class RestaurantPhoto(models.Model):
    photo = models.ImageField(upload_to = 'restaurant_pics', blank = True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Restaurant Photo: {}, {}".format(self.user, self.restaurant)

    def get_time(self):
        return localtime(self.created_at).strftime("%d %B %Y, %H:%M")

class RestaurantWaitingTime(models.Model):
    waiting_time = models.PositiveIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Restaurant Waiting Time: {}, {}, {}".format(self.user, self.restaurant, self.waiting_time)

class RestaurantCrowdCondition(models.Model):
    crowd_condition = models.PositiveIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return "Restaurant Crowd Condition: {}, {}, {}".format(self.user, self.restaurant, self.waiting_time)

class Dish(models.Model):
    name = models.CharField(max_length = 256)
    dish_profile_pic = models.ImageField(upload_to = 'dish_profile_pics', blank = True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    information = models.TextField(blank=True)
    verified = models.BooleanField(default = True)

    def __str__(self):
            return self.name

    def get_average_rating(self):
        lst = list(map(lambda x: x.rating, (self.dishrating_set.all())))
        return round(sum(lst)/len(lst), 1) if lst else 0

class DishRating(models.Model):
    rating = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Dish Rating: {}, {}, {}".format(self.user, self.dish, self.rating)

class DishReview(models.Model):
    review = models.TextField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Dish Review: {}, {}".format(self.user, self.dish)

    def get_average_rating(self):
        lst = list(map(lambda x: x.rating, (self.dishreviewrating_set.all())))
        return round(sum(lst)/len(lst), 1) if lst else 0

    def get_time(self):
        return localtime(self.created_at).strftime("%d %B %Y, %H:%M")

class DishReviewRating(models.Model):
    rating = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    dish_review = models.ForeignKey(DishReview, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Dish Review Rating: {}, {}".format(self.user, self.dish_review)
