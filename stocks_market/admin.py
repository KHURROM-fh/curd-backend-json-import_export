from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class StockModelAdmin(ImportExportModelAdmin):
    list_display=['date', 'tradecode', 'high', 'low', 'open', 'close', 'volume']
admin.site.register(models.StockData, StockModelAdmin)