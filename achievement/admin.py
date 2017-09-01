from django.contrib import admin

# Register your models here.
from .models import AchievementYear,Achievement
admin.site.register(AchievementYear)
admin.site.register(Achievement)