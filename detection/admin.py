from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.apps import apps

models = apps.get_models()  # Get all models in the app

for model in models:
    try:
        admin.site.register(model)  # Register each model
    except admin.sites.AlreadyRegistered:
        pass  # Skip if already registered

