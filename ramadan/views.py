from django.shortcuts import render, get_object_or_404

from .models import Greeter_Name, Festival_Info

from .forms import Greeter_Name_Form

greeter_form = Greeter_Name_Form()
share_name = text2 = text1 = x = ""
text1 = text2 = "XYZ"
all_text = Festival_Info.objects.all()
try:
    for x in all_text:
        pass
    text1  = x.text1
    text2  = x.text2
except AttributeError:
    pass

def ramadan_home(request):
    name = request.POST.get("name")
    if request.method == "POST":
        Greeter_Name.objects.create(name=name)
        Filter_Name = Greeter_Name.objects.filter(name=name)
        for name_id in Filter_Name:
            pass
        share_link = "http://festivalgreeting.herokuapp.com/" + ("ramadan/share/" + str(f"{name_id.pk}"))
        return render(request, "ramadan/ramadan_home.html", {"greeter_form":greeter_form, 'text1':text1, 'text2':text2, "name":name, "share_name":share_name, "share_link":share_link})
    return render(request, "ramadan/ramadan_home.html", {"greeter_form":greeter_form, 'text1':text1, 'text2':text2})


def share_ramadan_greeting(request, pk):
    target_name = get_object_or_404(Greeter_Name, pk=pk)
    return render(request, "ramadan/share_ramadan_greeting.html", {'text1':text1, 'text2':text2, "target_name":target_name, "greeter_form":greeter_form})
