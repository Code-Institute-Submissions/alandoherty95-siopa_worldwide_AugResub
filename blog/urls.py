from django.urls import path
from . import views


# Blog app URLs
urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>', views.delete_post,
         name='delete_post'),
]
