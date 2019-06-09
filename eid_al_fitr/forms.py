from django import forms

from .models import Eid_Greeter_Name

class Eid_Greeter_Name_Form(forms.ModelForm):
    class Meta:
        model = Eid_Greeter_Name
        fields = '__all__'

        
