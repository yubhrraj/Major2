from rest_framework import serializers
from .models import RecvData


class RecvDataSerializer(serializers.ModelSerializer):

    img = serializers.ImageField(max_length=None, allow_empty_file = False,)

    class Meta:
        model = RecvData
        fields = '__all__'



class KidDataSerializer(serializers.ModelSerializer):
    image = img = serializers.ImageField(max_length=None, allow_empty_file = False,)

    class Meta:
        mode = RecvData
        fields = '__all__'