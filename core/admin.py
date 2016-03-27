from core.models import Language
from django.contrib import admin


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
