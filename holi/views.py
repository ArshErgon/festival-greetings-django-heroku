from django.shortcuts import render, get_object_or_404

from .models import Add_Holi_Info, Greeter_Name_holi

from .forms import Greeter_Name_Holi_Form

all_text = Add_Holi_Info.objects.all()
share_name = text1 = text2 = ""
text1 = text2 = "XYZ"
for x in all_text:
    text1 = x.text1
    text2 = x.text2
add_greeter_form = Greeter_Name_Holi_Form()
def holi_home(request):
    add_greeter_form = Greeter_Name_Holi_Form(request.POST or None)
    if request.method == "POST":
        name = request.POST.get("name")
        Greeter_Name_holi.objects.create(name=name)
        filter_name = Greeter_Name_holi.objects.filter(name=name)
        for name_id in filter_name:
            pass
        share_link = "http://festivalgreeting.herokuapp.com/" + ("holi/share/") + str(f"{name_id.pk}")
        return render(request, "HOLI/holi_home.html", {'add_greeter_form':add_greeter_form, "name":name, "text1":text1, "text2":text2, "share_link":share_link})
    return render(request, "HOLI/holi_home.html", {'add_greeter_form':add_greeter_form, "text1":text1, "text2":text2})


def share_holi(request, pk):
    show_share_name = get_object_or_404(Greeter_Name_holi, pk=pk)
    return render(request, "HOLI/share_holi.html", {"text1":text1, "text2":text2, "show_share_name":show_share_name, 'add_greeter_form':add_greeter_form})

def error_404(request, exception):
    data = {"name":"127.0.0.1:8000"}
    return render(request, "error_404/index.html", data)
