from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'prix', 'created_at')
    search_fields = ('nom', 'adresse')
    list_filter = ('created_at',)
