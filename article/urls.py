from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("articles/", views.articles, name="articles"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addarticle/",views.addarticle,name="addarticle"),
    path("article/<int:id>",views.dashboard_detail,name="detail"),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete,name="delete"),
    path('article/comment/<int:id>' ,views.comment,name = "comment"),
]

    