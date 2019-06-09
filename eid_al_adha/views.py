from django.shortcuts import render, get_object_or_404

from .models import Bakra_Name_Model, Add_Bakra_Info

from .forms import Bakra_Name_Form

text1 = text2 = "XYZ"
bakra_form =  Bakra_Name_Form()
all_texts = Add_Bakra_Info.objects.all()
try:
    for x in full_text:
        pass
    text1 = x.text1
    text2 = x.text2
except:
    pass

def bakra_eid_home(request):
    name = request.POST.get("name")
    if request.method == "POST":
        Bakra_Name_Model.objects.create(name=name)
        filter_data = Bakra_Name_Model.objects.filter(name=name)
        for name_id in filter_data:
            pass
        share_link = "http://festivalgreeting.herokuapp.com/" + ("bakra/share/") + str(f"{name_id.pk}")
        return render(request,"bakra/bakra_home.html", {"bakra_form":bakra_form, "name":name, "text1":text1, "text2":text2, "share_link":share_link})
    return render(request,"bakra/bakra_home.html", {"bakra_form":bakra_form, "text1":text1, "text2":text2})


def share_bakra_name(request, pk):
    show_greeter_name = get_object_or_404(Bakra_Name_Model, pk=pk)
    return render(request, "bakra/share_bakra.html", {'show_greeter_name':show_greeter_name, "bakra_form":bakra_form, "text1":text1, "text2":text2})
