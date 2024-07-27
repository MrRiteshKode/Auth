from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages 
from django.views import View
from gallery.forms import AboutForm
from gallery.models import About
from gallery.models import Image,User

def home(request):
    allUsers = User.objects.all()
    return render(request, 'home.html', {'allUsers':allUsers})

def Handlelogin(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        if request.method == "POST":
            username = request.POST.get("name")
            password = request.POST.get("password")

            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("home")
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("home")      
        return render(request, 'login.html')

def Handlesignup(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        if request.method == "POST":
            username = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            print(username,email,password)
            
            if len(username) > 0 and len(email) > 0 and len(password)>0:
                # Create the user
                myuser = User.objects.create_user(username, email, password)
                myuser.save()                
                messages.success(request,"Your account created successfully, now login.")
                return redirect("home")
            else:
                messages.error(request,"Something error occured, Please fill form correctly.")
        return render(request, 'signup.html')

def Handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')

    
def profileShow(request,profile_name):
    allUsers = User.objects.all()
    try:
        user = User.objects.get(username=profile_name)      
    except:
        return render(request,'profiles.html',{'msg':"ACCOUNT NOT FOUND !!",'allUsers':allUsers})
    else:
        Images = Image.objects.filter(user=user)
        if not Images:
            return render(request,'profiles.html',{'msg':'NOT IMAGES FOUND !!','allUsers':allUsers})
        else:
            return render(request,'profiles.html',{'all_imgs':Images,'allUsers':allUsers})
        
    
# class based view
class AboutPage(View):
    allUsers = User.objects.all()
    def get(self,request):
        try:
            about = About.objects.get(user=request.user)
        except Exception as e: 
            
            about = About(fullName="",about="",user=request.user)
            about.save()
        finally:
            about = About.objects.get(user=request.user)
            fm = AboutForm(instance=about)
            return render(request,'about.html', {'form':fm,'allUsers':AboutPage.allUsers})     
    
    def post(self, request):
        about = About.objects.get(user=request.user)
        fm = AboutForm(request.POST,instance=about)
        if fm.is_valid:
            fm.save()
            messages.success(request,"Your data saved successfully.")
            return redirect('about')

