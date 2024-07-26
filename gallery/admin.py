from django.contrib import admin
from .models import Image, About

# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ['id', 'photo','user','date']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
	list_display = ['id', 'fullName','about','user']