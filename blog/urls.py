from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_blogcontent, name="blog"),
    path('<str:slug>', views.show_post, name="show_post"),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>', views.delete_post,
         name='delete_blogpost'),
]
