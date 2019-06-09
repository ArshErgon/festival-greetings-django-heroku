from django import forms

from .models import Greeter_Name_holi

class Greeter_Name_Holi_Form(forms.ModelForm):
    class Meta:
        model = Greeter_Name_holi
        fields = ["name"]
