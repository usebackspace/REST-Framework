from django.contrib import admin
from .models import Avenger
# Register your models here.
@admin.register(Avenger)
class AvengerAdmin(admin.ModelAdmin):
    list_display=['id','name','heroic_name']
