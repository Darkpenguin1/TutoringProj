# take a model/obj and turns it into a json obj
from rest_framework.serializers import ModelSerializer 
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'