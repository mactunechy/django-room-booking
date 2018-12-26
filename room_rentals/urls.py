from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('rooms.urls')),
    path('accounts/', include('allauth.urls')),
    path('album/',include('album.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('contact/',include('landing.urls'))
       
]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)