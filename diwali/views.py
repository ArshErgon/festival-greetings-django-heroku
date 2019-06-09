from django.shortcuts import render, get_object_or_404

from .models import Greeter_Name_Diwali, Add_Diwali_Info

from .forms import Greeter_Name_Diwali_Form

greeter_form = Greeter_Name_Diwali_Form()
all_text = Add_Diwali_Info.objects.all()
share_link =  ""
text1 = text2 = "XYZ"
try:
    for x in all_text:
        text1 = x.text1
        text2 = x.text2
except:
    pass

def diwali_home(request):
    name = request.POST.get("name")
    if request.method == "POST":
        Greeter_Name_Diwali.objects.create(name=name)
        filter_name = Greeter_Name_Diwali.objects.filter(name=name)
        for name_id in filter_name:
            pass
        share_link = "http://festivalgreeting.herokuapp.com/" + ("diwali/share/") + str(f"{name_id.pk}")
        return render(request, "DIWALI/diwali_home.html", {"greeter_form":greeter_form, "text1":text1, "text2":text2, "name":name, "share_link": share_link})
    return render(request, "DIWALI/diwali_home.html", {"greeter_form":greeter_form, "text1":text1, "text2":text2})

def share_diwali(request, pk):
    share_name = get_object_or_404(Greeter_Name_Diwali, pk=pk)
    return render(request, "DIWALI/share_diwali.html", {"share_name":share_name, 'greeter_form':greeter_form})
