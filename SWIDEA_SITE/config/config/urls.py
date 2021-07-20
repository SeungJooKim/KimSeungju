from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Ideas",include("Ideas.urls")),
    path("devtools/",include("DevTools.urls")),
    path('', lambda req : redirect('Ideas:idea_list'),name='root')
]
