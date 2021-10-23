from django.urls import path
from main import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.sign_in, name='sign_in'),
    path('logout/',views.logout, name='logout'),
    path('new_receita/',views.receita, name='receita'),
    path('new_despesa/',views.despesa, name='despesa'),
    path('outros/',views.outros, name='outros'),
]