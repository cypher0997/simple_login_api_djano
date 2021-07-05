from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name="post_method"),
    path('login_response/', views.login_response, name="log_R")
]
