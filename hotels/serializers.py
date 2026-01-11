from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = [
            'id',
            'nom',
            'adresse',
            'prix',
            'image',
            'image_url',
            'created_at',
            'updated_at',
        ]

    def get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            # Force HTTPS
            if url.startswith('http://'):
                url = url.replace('http://', 'https://')
            return url
        return None
