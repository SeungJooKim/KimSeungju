from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('blog/', include('blog.urls') ),
    path('', lambda req : redirect('blog:post_list'),name='root'), #url reverse를 쓰면 좋음
]
