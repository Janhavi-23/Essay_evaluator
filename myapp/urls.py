from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('logout', views.logout_view),
    path('submit_essay', views.submit_essay, name='submit_essay')
]