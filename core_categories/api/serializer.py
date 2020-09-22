from rest_framework.serializers import ModelSerializer
from core_categories.models import CategoriesRoiValue

class CategorieSerializer(ModelSerializer):
    class Meta:
        model = CategoriesRoiValue
        fields = '__all__'