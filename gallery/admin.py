from django.contrib import admin
from .models import Image, About,User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ['photo','user','date']
	
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
	pass