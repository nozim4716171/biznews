from http.client import HTTPResponse
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from newsapp.forms import ContactForm
from newsapp.models import yangiliklar, Kategoriya
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
def AsosiySahifaView(request):
    category_list = Kategoriya.objects.all()
    news_list1 = yangiliklar.objects.all().order_by('yuklangan_vaqti')[0:3]
    news_list2 = yangiliklar.objects.all().order_by('yuklangan_vaqti')[3:7]
    url = ' https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/pair/USD/UZS'
    url2='https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/pair/RUB/UZS'
    url3='https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/pair/EUR/UZS'
    natija3=requests.get(url3)
    natija2=requests.get(url2)
    natija = requests.get(url)
    eur=int(natija3.json()['conversion_rate'])
    uzs=int(natija.json()['conversion_rate'])
    rub=int(natija2.json()['conversion_rate'])
    
    context = {
        'category_list': category_list,
        'news_list1': news_list1,
        'news_list2': news_list2,
        'uzs': uzs,
        'rub': rub,
        'eur': eur
    }
    return render(request, 'index.html', context)

def ContactSahifaView(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HTTPResponse("<h1>Biz siz bilan tez orada bog'lanamiz!</h1>")
    news_list1 = yangiliklar.objects.all().order_by('yuklangan_vaqti')[0:3]
    category_list = Kategoriya.objects.all()
    context = {
        'form': form,
        'news_list1': news_list1,
        'category_list': category_list
    }
    return render(request, 'contact.html', context)


def NewsDetailView(request,slug):
    news = get_object_or_404(yangiliklar, slug=slug, status=yangiliklar.Status.yuklash)
    news_list1 = yangiliklar.objects.all().order_by('yuklangan_vaqti')[0:3]
    category_list = Kategoriya.objects.all()
    context = {
        'news': news,
        'news_list1': news_list1,
        'category_list': category_list
    }
    return render(request, 'single.html',context)


class QidirishView(ListView):
    model = yangiliklar
    template_name = 'qidirish.html'
    context_object_name = 'qidirish_natijasi'
    
    def get_queryset(self):
        data = self.request.GET.get('q')
        return yangiliklar.objects.filter(
            Q(nomi__icontains=data)|Q(matn__icontains=data)
        )
        
  
class YangilikUpdateView(UpdateView):
    model = yangiliklar
    fields = ('nomi','slug','matn','rasm','kategoriya','status')
    template_name = 'yangilash.html'
    

class YangilikDeleteView(DeleteView):
    model = yangiliklar
    template_name = 'uchirish.html'
    success_url = reverse_lazy("home")


class YangilikCreateView(CreateView):
    model = yangiliklar
    fields = ('nomi','slug','matn','rasm','kategoriya','status')
    template_name = 'yaratish.html'
