from django.urls import path
from . import views
app_name ='Ideas'
urlpatterns = [
    path('', views.idea_list, name='idea_list'),
]
