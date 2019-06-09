from django.shortcuts import render, get_object_or_404

from .forms import Eid_Greeter_Name_Form

from .models import Eid_Greeter_Name, Add_Eid_Info

eid_form = Eid_Greeter_Name_Form()
full_text = Add_Eid_Info.objects.all()
share_name = text2 = text1 = x = ""
text1 = text2 = "XYZ"
try:
    for x in full_text:
        pass

    text1 = x.text1
    text2 = x.text2
except AttributeError:
    pass

def eid_al_fitr_home(request):
    name = request.POST.get("name")
    if request.method == "POST":
        Eid_Greeter_Name.objects.create(name=name)
        filter_data = Eid_Greeter_Name.objects.filter(name=name)
        for name_id in filter_data:
            pass
        share_link = "http://festivalgreeting.herokuapp.com/" + ("eid/share/") + str(f"{name_id.pk}")
        return render(request, "EID/eid_al_fitr_home.html", {"eid_form":eid_form, "text1":text1, "text2":text2, "share_link":share_link, "name":name})
    return render(request, "EID/eid_al_fitr_home.html", {"eid_form":eid_form, "text1":text1, "text2":text2})

def share_eid_al_fitr(request, pk):
    show_greeter_name = get_object_or_404(Eid_Greeter_Name, pk=pk)
    return render(request, "EID/share_eid_al_fitr.html", {'show_greeter_name':show_greeter_name, "text1":text1, "text2":text2})
