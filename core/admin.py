from django.contrib import admin
from .models import Car
from django.utils.html import format_html

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "title", "model_year", "daily_price", "status", "preview")
    search_fields = ("brand", "title", "plate_no")
    list_filter = ("status", "transmission", "model_year")

    def preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover;"/>', obj.image_url)
        return "-"
    preview.short_description = "Image"
