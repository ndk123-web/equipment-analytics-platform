from django.contrib import admin
from .models import Dataset

# Register your models here.
@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "uploaded_by",
        "id",
        "uploaded_at",
        "total_rows",
    )
    
    list_filter = ("uploaded_by", "uploaded_at")
    search_fields = ("name",)