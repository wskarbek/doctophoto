from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('examination/<int:examination_id>', views.examination, name='examination'),
    path('welcome', views/signup, name='signup')
]