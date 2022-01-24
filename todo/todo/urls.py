from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todoapp.views import TodoViewSet

r = DefaultRouter()
r.register("todo", TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(r.urls)),
]
