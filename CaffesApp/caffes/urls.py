"""
List of posts and comments urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('caffe/<int:pk>/', views.detail_view, name='detail'),
    path('caffe/<int:pk>/add_comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('caffe/<int:caffe_pk>/comment/<int:comment_pk>/remove/',
         views.comment_remove, name='comment_remove'),
    path('caffe/<int:caffe_pk>/comment/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'),
    ]
