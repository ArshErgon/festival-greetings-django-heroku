from django.urls import path

from . import views

app_name = "diwali"
urlpatterns  = [
    path("", views.diwali_home, name="diwali_home"),
    path("share/<int:pk>/", views.share_diwali, name="share_diwali"),
]
