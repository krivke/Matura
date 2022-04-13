from django.urls import reverse
from django.shortcuts import redirect, render
from .forms import NoviNaslovForm
# Create your views here.
def home(request):
    print(request.POST)
    form = NoviNaslovForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse("hrvatski"))
    #TODO: kad napravi novi naslov neka se napravi i template/js/css fileovi - da jako ubrzam
    return render(request,"lekcije/prva.html",context={"form":form})