from django import forms

from .models import Greeter_Name

class Greeter_Name_Form(forms.ModelForm):
    class Meta:
        model = Greeter_Name
        fields = "__all__"
