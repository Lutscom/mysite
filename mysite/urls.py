from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('vrzhserv/', include('vrzhserv.urls')),
    path('admin/', admin.site.urls),
]
