from rest_framework.viewsets import ModelViewSet
from core_categories.models import CategoriesRoiValue
from core_categories.api.serializer import CategorieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class CategoriesViewSet(ModelViewSet):
    queryset = CategoriesRoiValue.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
