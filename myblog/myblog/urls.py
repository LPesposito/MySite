from django.contrib import admin
from django.urls import path
from blog.views import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home",views.home),
    path("posts/", views.Posts, name="Posts"),
]
