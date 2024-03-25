from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Presale


@admin.register(Presale)
class PresaleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'logo',
        'chain',
        'price',
        'quantity',
        'start_date',
        'end_date',
        'date_added'
    )
