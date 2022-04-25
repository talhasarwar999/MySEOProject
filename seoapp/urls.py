
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
]