from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(FarmDetail)
admin.site.register(CropData)
admin.site.register(LivestockData)
admin.site.register(WaterUsage)
admin.site.register(MachineryUse)