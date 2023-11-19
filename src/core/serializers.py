from rest_framework import serializers

from src.core.models import Data


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'
        extra_kwargs = {
            "timestamp": { "read_only": True },
            "record": { "read_only": True }
        }
