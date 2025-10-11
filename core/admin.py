from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id','brand','title','model_year','daily_price','status','plate_no')
    list_filter = ('status','transmission','brand','model_year')
    search_fields = ('brand','title','plate_no')
