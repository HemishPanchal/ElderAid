"""
URL configuration for elder_aid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from elder_bookings.admin import admin_site
urlpatterns = [
    path('admin/',admin_site.urls),
    path('',views.home,name='home'),
    path('about/',views.about_view,name='about'),
    path('contacts/',views.contacts_view,name='contacts'),
    path('special/',views.special_view,name='special'),
    path('admin/', admin.site.urls),
    path('registration/',include('user_register.urls')),
    path('services/',include('elder_services.urls')),
    path('subservices/',include('elder_subservices.urls')),
    path('book/',include('elder_bookings.urls')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

