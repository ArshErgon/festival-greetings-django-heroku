from django.contrib import admin

# Register your models here.
from .models import Add_Eid_Info,  Eid_Greeter_Name

admin.site.register(Eid_Greeter_Name)
admin.site.register(Add_Eid_Info)
