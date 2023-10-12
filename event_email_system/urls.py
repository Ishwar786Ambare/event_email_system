"""
URL configuration for event_email_system project.

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
from django.urls import path

from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-event-emails/', views.SendEmailView.as_view(), name='send-event-emails'),
    path('retrieve-event-data/<int:event_id>/', views.RetrieveEventData.as_view(), name='retrieve-event-data'),
    path('retrieve-email-template/<int:event_id>/', views.RetrieveEmailTemplate.as_view(), name='retrieve-email-template'),
]
