from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=100)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="datasets")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    total_rows = models.IntegerField()
    avg_usage_hours = models.FloatField()
    avg_power = models.FloatField()

    equipment_distribution = models.JSONField()

    def __str__(self):
        return f"{self.name} ({self.uploaded_by.username})"