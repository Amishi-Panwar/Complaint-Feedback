from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url,include
router=routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('complaintnfeedback.urls')),
]
