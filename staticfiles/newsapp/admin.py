from django.contrib import admin
from .models import yangiliklar,Kategoriya, Contact

# Register your models here.


# admin.site.register(yangiliklar)
# admin.site.register(Kategoriya)

@admin.register(yangiliklar)
class yangiliklarAdmin(admin.ModelAdmin):
    list_display = ['nomi','kategoriya','yuklangan_vaqti','status']
    list_filter = ['status', 'yaratilgan_vaqti','yuklangan_vaqti' ]
    prepopulated_fields = {'slug': ('nomi',)}
    date_hierarchy = 'yuklangan_vaqti' 
    search_fields = ['nomi','matn']
    ordering = ['status','yuklangan_vaqti']
    
    
@admin.register(Kategoriya)
class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ['id','nomi']
    search_fields = ['nomi']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['ism', 'email']
    search_fields = ['ism', 'email']