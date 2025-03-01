"""
URL configuration for Authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="Authentication System"
admin.site.site_title="Authentication Panel"
admin.site.index_title="Welcome to Authentication Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/', views.Handlelogin, name='login'),
    path('signup/', views.Handlesignup, name='signup'),
    path('logout/', views.Handlelogout, name="logout"),
    path('profile/', include('gallery.urls')),
    path('about/', views.AboutPage.as_view() , name="about" ),
    path('<str:profile_name>/',views.profileShow),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
