from django.contrib import admin
from trademark import models


# class StoreAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Brand)
# admin.site.register(models.StoreGroup)
# admin.site.register(models.OpeningPeriod)
# admin.site.register(models.StoreStock)
