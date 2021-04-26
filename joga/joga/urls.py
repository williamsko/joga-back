"""joga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from apps.customer import urls as customer_api_urls
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

admin.site.site_header = 'Joga admin'
admin.site.site_title = 'Joga admin'
admin.site.index_title = 'Welcome to  Joga platform administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include(customer_api_urls)),
]
