from rest_framework.serializers import ModelSerializer

from applessons.models import Applessons


class SerializersApplessons(ModelSerializer):

    class Meta:
        model = Applessons
        fields = '__all__'
