from core.models import Language, Country
from django.contrib import admin


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('alpha2', 'English',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('alpha3', 'name', 'population',)
