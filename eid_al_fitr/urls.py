from django.urls import path

from . import views

app_name = "eid_al_fitr"

urlpatterns = [
    path("", views.eid_al_fitr_home, name="eid_al_fitr_home"),
    path("share/<int:pk>/", views.share_eid_al_fitr),
]
