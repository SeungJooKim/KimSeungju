from django.contrib import admin
from django.urls import path
from .views import PostCreateView
from . import views
from django.conf.urls.static import static
from django.conf import settings 

app_name ='posts'
urlpatterns = [
    path('list/', views.post_list, name ="post_list"),
    path('create/', PostCreateView.as_view(), name ="post_create"),
    path('delete_comment/', views.delete_comment, name="delete_comment"),
    path('add_comment/', views.add_comment, name="add_comment"),
    path('like/', views.like,name="like"),
]
