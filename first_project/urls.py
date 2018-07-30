"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('signup/', views.user_signup, name = "signup"),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('profile/<int:pk>', views.user_profile, name = "profile"),
    path('edit_profile/<int:pk>', views.edit_profile, name = "edit_profile"),
    path('edit_restaurant_review/<int:pk>', views.edit_restaurant_review, name = "edit_restaurant_review"),
    path('delete_restaurant_review/<int:pk>', views.delete_restaurant_review, name = "delete_restaurant_review"),
    path('dish_edit_review/<int:pk>', views.edit_dish_review, name = "edit_dish_review"),
    path('dish_delete_review/<int:pk>', views.delete_dish_review, name = "delete_dish_review"),
    path('delete_restaurant_photo/<int:pk>', views.delete_restaurant_photo, name = "delete_restaurant_photo"),
    path('add_restaurant_photo/<int:pk>', views.add_restaurant_photo, name = "add_restaurant_photo"),
    path('restaurant/<int:pk>', views.restaurant_page, name = "restaurant"),
    path('restaurant_add_rating/<int:pk>', views.add_restaurant_rating, name = "add_restaurant_rating"),
    path('restaurant_add_review/<int:pk>', views.add_restaurant_review, name = "add_restaurant_review"),
    path('restaurant_add_waiting_time/<int:pk>', views.add_restaurant_waiting_time, name = "add_waiting_time"),
    path('restaurant_add_crowd_condition/<int:pk>', views.add_restaurant_crowd_condition, name = "add_crowd_condition"),
    path('restaurant_add_review_rating/<int:pk>', views.add_restaurant_review_rating, name = "add_restaurant_review_rating"),
    path('dish_add_review_rating/<int:pk>', views.add_dish_review_rating, name = "add_dish_review_rating"),
    path('dish/<int:pk>', views.dish_page, name = "dish"),
    path('dish_add_rating/<int:pk>', views.add_dish_rating, name = "add_dish_rating"),
    path('dish_add_review/<int:pk>', views.add_dish_review, name = "add_dish_review"),
    path('add_dish/<int:pk>', views.add_dish, name = "add_dish"),
    path('search/', views.search, name = "search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
