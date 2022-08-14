from django.urls import path
# from .views import index
from searchdb import views

urlpatterns = [
    path('', views.index,name='index'),
    path('natega',views.natega,name='natega')
   
]