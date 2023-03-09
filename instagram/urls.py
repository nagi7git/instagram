"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from order_form import views
from django.conf import settings
from django.conf.urls.static import static

order_form = [
    path('', views.order_create, name="order_create"),
    path('status', views.status, name="status"),  
    path('order', views.order, name="order"),
    path('order/<int:pk>/delete', views.order_delete, name="order_delete"),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(order_form))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)