from django import forms

from .models import Bakra_Name_Model

class Bakra_Name_Form(forms.ModelForm):
    class Meta:
        model = Bakra_Name_Model
        fields = '__all__'

        
