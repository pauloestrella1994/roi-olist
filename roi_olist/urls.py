from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core_categories.api.viewsets import CategoriesViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'categories_roi', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
]
