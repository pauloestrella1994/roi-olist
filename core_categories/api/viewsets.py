from rest_framework.viewsets import ModelViewSet
from core_categories.models import CategoriesRoiValue
from core_categories.api.serializer import CategorieSerializer

class CategoriesViewSet(ModelViewSet):
    queryset = CategoriesRoiValue.objects.all()
    serializer_class = CategorieSerializer
