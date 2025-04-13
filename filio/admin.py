from django.contrib import admin
from .models import Resume  # Import Resume model

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'pdf')  # Show name and PDF file in the admin panel
    search_fields = ('name',)  # Allow searching by name