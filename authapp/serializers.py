from rest_framework import serializers
from .models import product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('pid','pname','pcost')