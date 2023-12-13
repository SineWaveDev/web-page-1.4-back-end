# serializers.py
from rest_framework import serializers


class CalculateTaxSerializer(serializers.Serializer):
    BusinessProfession = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    # Add other fields as needed
