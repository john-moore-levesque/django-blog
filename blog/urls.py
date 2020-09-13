from django.urls import path
from blog import views


urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("post/new/", views.PostCreateView.as_view(), name="blog_create"),
    path("<author>", views.blog_home, name="blog_author"),
    path("<author>/<slug>/", views.blog_detail, name="blog_detail"),
    path("<author>/<slug>/update/", views.PostUpdateView.as_view(), name="blog_update"),
    path("<author>/<slug>/delete/", views.PostDeleteView.as_view(), name="blog_delete"),
    path("<author>/category/<slug>", views.blog_home, name="blog_author_category"),
    path("category/<slug>", views.blog_home, name="blog_category"),
]
