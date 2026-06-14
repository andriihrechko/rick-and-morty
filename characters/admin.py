from django.contrib import admin

from characters.models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("api_id", "name", "status", "species", "gender")
    search_fields = ("name",)
    list_filter = ("status", "species", "gender")
    ordering = ("name",)
