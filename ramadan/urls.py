from django.urls import path

from . import views

app_name = "ramadan"

urlpatterns = [
    path("", views.ramadan_home, name="ramadan_home"),
    path("share/<int:pk>/", views.share_ramadan_greeting, name="ramadan_share"),
]
