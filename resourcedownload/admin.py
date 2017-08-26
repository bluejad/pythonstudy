from django.contrib import admin

# Register your models here.

from .models import downloadstation, Querystation

admin.site.register(downloadstation)
admin.site.register(Querystation)