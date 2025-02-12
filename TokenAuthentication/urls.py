
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Authentication.urls')),
    path('api-auth/',include('rest_framework.urls')),

]
