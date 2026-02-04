from django.db import models
from django.contrib.auth.models import User

class SkinDiseaseDetection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional link to logged-in user
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    uploaded_image = models.ImageField(upload_to='uploads/')
    predicted_disease = models.CharField(max_length=50)
    prediction_confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} - {self.predicted_disease} ({self.timestamp})"



# Create your models here.
