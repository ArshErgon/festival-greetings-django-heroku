from django import forms

from .models import Greeter_Name_Diwali

class Greeter_Name_Diwali_Form(forms.ModelForm):
    class Meta:
        model = Greeter_Name_Diwali
        fields = '__all__'
