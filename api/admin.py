from django.contrib import admin

# Register your models here.
from api import models

class AcutionModelAdmin(admin.ModelAdmin):
    list_display = ['topic','status']
admin.site.register(models.Acution)
admin.site.register(models.Details)
admin.site.register(models.NewDetails)
admin.site.register(models.Payment)
admin.site.register(models.Browse)