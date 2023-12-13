from django.contrib import admin
from .models import Court

# Register your models here.

class CourtAdmin(admin.ModelAdmin):
  list_display = ("courtname", "courttype", "city")
  
admin.site.register(Court, CourtAdmin)