from django.urls import path

from . import views

app_name = "eid_al_adha"
urlpatterns = [
    path("", views.bakra_eid_home, name='eid_al_adhar_home'),
    path("share/<int:pk>/", views.share_bakra_name),
]
