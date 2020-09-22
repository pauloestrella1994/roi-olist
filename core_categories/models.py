from django.db import models

class CategoriesRoiValue(models.Model):
    category_name = models.CharField(max_length=100, null=False)
    roi_value = models.DecimalField(decimal_places=10, max_digits=20, null=False)

    def __str__(self):
        return self.category_name