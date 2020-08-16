from . import views
from django.urls import path

urlpatterns = [
    path('blogs/', views.PostList.as_view(), name='home'),
    path('',views.home.as_view(),name='blog'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('contacts/',views.contact.as_view(),name='contacts'),
    path('tags/<int:pk>', views.taglist.as_view(),name='tags'),
]