
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
    path('businessale/',views.businessale,name='businessale'),
    path('businessrapid/',views.businessrapid,name='businessrapid'),
    path('businessuccess/',views.businessuccess,name='businessuccess'),
    path('chelseadentalclinic/',views.chelseadentalclinic,name='chelseadentalclinic'),
    path('team/',views.team,name='team'),
    path('electric_mr/',views.electric_mr,name='electric_mr'),
    path('ratedpeople/',views.ratedpeople,name='ratedpeople'),
]
