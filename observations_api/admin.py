from django.contrib import admin
from .models import User, Species

@admin.register(Species)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'sc_name']

