from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="detail-post"),
    path("<slug:slug>/add-comment", views.AddCommentView.as_view(), name="add-comment")
]
