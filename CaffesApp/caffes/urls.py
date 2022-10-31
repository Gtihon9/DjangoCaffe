from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail_view, name='detail'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    ]