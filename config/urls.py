from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path

urlpatterns = [
       path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
