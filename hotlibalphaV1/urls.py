from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from hotlibrary.views.indexviews import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('', include('hotlibrary.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root="settings.STATIC_ROOT")
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root="settings.MEDIA_ROOT")

