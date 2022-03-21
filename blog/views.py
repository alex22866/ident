from django.shortcuts import render
from django.utils.text import Truncator

from .models import *


def base(request):
    cats = DentIn.objects.all()

    return render(request, 'base.html', locals())

def index(request):
    sliders = Slider.objects.all()
    banner = Banner.objects.first()
    page = Page.objects.all()
    new = New.objects.all()
    about = About.objects.all()
    cats = DentIn.objects.all()
    context = {"sliders": sliders, "banner":
                            banner, "page": page,
                            "new": new, "service": service, "about": about, 'cats': cats}
    return render(request, 'index.html',context)



def new(requst):
    new = New.objects.filter(is_active=True)[:4]
    read_more = Truncator(New.description).words(14, truncate='...Читать далее')
    return render(requst, 'new.html', locals())


def product(request, pk):
    dentin = DentIn.objects.filter(pk=pk)
    # dentOb = DentOb.objects.get(pk=pk)
    return render(request, 'catalog.html', locals())


def about(request):
    return render(request, 'about.html')



def service(request):
    service = Service.objects.all()
    context = {"service": service,}
    return render(request, 'service.html', context)
