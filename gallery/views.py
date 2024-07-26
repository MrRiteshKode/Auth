from django.shortcuts import render,redirect    
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib import messages 
from .models import Image
import os

# Create your views here.
@login_required(login_url="/login")
def profile(request):
    if request.method == "POST":
        img = request.FILES["image"]
        if img:
            new_img = Image(photo=img, user=request.user)
            new_img.save()
            messages.success(request, "successfully upload you image !")
    all_imgs = Image.objects.filter(user=request.user)  
    allUsers = User.objects.all()
    return render(request, 'profile.html', {'all_imgs':all_imgs,'allUsers':allUsers})


def HandleImg(request):
    if request.method == "POST":
        img = request.POST["image"]
        if img:
            check_img = Image.objects.filter(photo=img,user=request.user)
            if check_img is not None:
                check_img.delete()
                os.remove(f"media/{img}")
                messages.success(request, "successfully delete you image !")
    return redirect("profile")

def new(request):
    return HttpResponse("helo")
