
from . import views

from django.urls import path

urlpatterns = [

    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
path('', views.PostList.as_view(), name='home'),

]