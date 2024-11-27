
from django.contrib import admin
from django.urls import path
from messapp import views

urlpatterns = [
    path('create',views.create),
    path('dashboard',views.dashboard),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),

]
