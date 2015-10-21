from rest_framework import serializers
from settings.NetworkConnectivity.models import Network


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ('id', 'geoLocation')

    def create(self, validated_data):
        return Network.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.geoLocation = validated_data.get('geoLocation', instance.geoLocation)
        instance.save()
        return instance
