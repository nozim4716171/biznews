from django.urls import path
from django.urls import include
from newsproject import settings
from django.conf.urls.static import static
from newsapp.views import AsosiySahifaView,ContactSahifaView,NewsDetailView,QidirishView,YangilikCreateView,YangilikDeleteView,YangilikUpdateView

urlpatterns = [
    path('', AsosiySahifaView, name='home'),
    path('contact/', ContactSahifaView, name='contact'),
    path('news/<str:slug>/',NewsDetailView, name='newsdetail'),
    path('news/<str:slug>/edit/',YangilikUpdateView.as_view(), name='newsedit'),
    path('news/<str:slug>/delete/',YangilikDeleteView.as_view(), name='newsdelete'),
    path('create/',YangilikCreateView.as_view(), name='newscreate'),
    path('search/',QidirishView.as_view(),name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)