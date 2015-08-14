from django.contrib import admin

from .models import Area, Period, ResearchEvent, Settlement, Site, Finds, Interpretation

admin.site.register(Area)
admin.site.register(Period)
admin.site.register(ResearchEvent)
admin.site.register(Settlement)
admin.site.register(Site)
admin.site.register(Finds)
admin.site.register(Interpretation)
# Register your models here.