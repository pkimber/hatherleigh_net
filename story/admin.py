from django.contrib import admin

from .models import Area


class AreaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
