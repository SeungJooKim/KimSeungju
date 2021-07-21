from django.urls import path
from . import views

app_name ='Ideas'

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('create/', views.idea_create, name ='idea_create'),
    path('<int:pk>/', views.idea_detail, name ='idea_detail'),
    path('<int:pk>/delete/',views.idea_delete, name='idea_delete'),
    path('<int:pk>/update/', views.idea_update, name='idea_update'),
    path('interest_add/', views.interest_add, name="interest_add"),
    path('interest_minus/', views.interest_minus, name="interest_minus"),
    
]
