from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Hotel
from .serializers import HotelSerializer
from drf_yasg.utils import swagger_auto_schema


class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all().order_by('-created_at')
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    @swagger_auto_schema(operation_summary="Lister tous les hôtels")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Récupérer un hôtel par ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Créer un nouvel hôtel")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Modifier un hôtel existant")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Supprimer un hôtel")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)