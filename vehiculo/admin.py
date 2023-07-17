
# Register your models here.
from django.contrib import admin
from .models import Auto


class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'serial_carroceria',
                    'serial_motor', 'categoria', 'precio')
    ordering = ('marca', 'modelo')


admin.site.register(Auto, AutoAdmin)
