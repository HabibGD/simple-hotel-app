from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# drf-yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Red Product Hotel API",
        default_version='v1',
        description="API pour gérer les hôtels, avec CRUD complet et images Cloudinary",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="habibdiallohd08@gmail.com"),
        license=openapi.License(name="Gandal-Dev Licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('api/', include('hotels.urls')),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ReDoc (optionnel)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

