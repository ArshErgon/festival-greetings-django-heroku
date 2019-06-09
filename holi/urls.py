from django.urls import path

from . import views

app_name = "holi"
urlpatterns = [
    path("", views.holi_home, name="holi_home"),
    path("share/<int:pk>/", views.share_holi, name="share_holi"),
]
