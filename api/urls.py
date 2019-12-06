from django.urls import path
from .views import (ListView,CreateAPIView,DeleteView,DeleteAll,Status)
# from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
   

    path('get/',ListView.as_view(), name='get'),
    path('delete/<int:id>/',DeleteView.as_view(), name='delete'),
    path('add/',CreateAPIView.as_view(), name='add'),
    path('deleteall/',DeleteAll.as_view(), name='delete_all'),
    path('status/<int:id>/',Status.as_view(), name='status'),





]