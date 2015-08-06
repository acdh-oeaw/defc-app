from django.contrib import admin

from .models import Area, Period, ResearchEvent, Site, Finds

admin.site.register(Area)
admin.site.register(Period)
admin.site.register(ResearchEvent)
admin.site.register(Site)
admin.site.register(Finds)
# Register your models here.