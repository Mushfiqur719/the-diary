from django.contrib import admin
from . models import Case,CaseType,Court,PoliceStation

# Register your models here.

admin.site.register(Case)
admin.site.register(CaseType)
admin.site.register(Court)
admin.site.register(PoliceStation)