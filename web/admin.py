from django.contrib import admin
from .models import Member
from import_export.admin import ImportExportModelAdmin

@admin.register(Member)
class userdat(ImportExportModelAdmin):
    pass

# Register your models here.
