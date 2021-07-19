from django.contrib import admin
from django.http import HttpResponse
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

def mysum(request, x, y):
    result = x+y
    return HttpResponse('result={}'.format(result))


urlpatterns = [  # 순서가 존재!
    path('admin/', admin.site.urls),
    path('mysum/<int:x>/<int:y>/', mysum),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
