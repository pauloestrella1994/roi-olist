from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core_categories.api.viewsets import CategoriesViewSet


router = routers.DefaultRouter()
router.register(r'categories_roi', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
