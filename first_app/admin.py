from django.contrib import admin
from first_app.models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(Restaurant)
admin.site.register(OpeningHours)
admin.site.register(RestaurantRating)
admin.site.register(RestaurantReview)
admin.site.register(RestaurantPhoto)
admin.site.register(RestaurantReviewRating)
admin.site.register(RestaurantWaitingTime)
admin.site.register(RestaurantCrowdCondition)
admin.site.register(Dish)
admin.site.register(DishRating)
admin.site.register(DishReview)
admin.site.register(DishReviewRating)
