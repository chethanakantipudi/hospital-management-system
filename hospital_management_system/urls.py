"""HospitalManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include  # Include to handle app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),  # Include app-specific URLs
]
