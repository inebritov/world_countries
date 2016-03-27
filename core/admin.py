from core.models import Language
from django.contrib import admin


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('alpha2', 'English',)
