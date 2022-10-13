from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail_view, name='detail'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post')
    ]