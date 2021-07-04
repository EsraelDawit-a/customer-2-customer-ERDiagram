from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as A
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
# Register your models here.

class CustomUserAdmin(A):
    list_display = ['username','contac_info','optional_adress','first_name','last_name' ]


class CatagorieAdmin(admin.ModelAdmin):
    list_display = ['name','created_date','decription']

class SubCatagorieAdmin(admin.ModelAdmin):
    list_display = ['name','created_date','decription','fields']

class AdAdmin(admin.ModelAdmin):
    list_display = ['name','state','city','area','created_date','seller']

admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(Catagorie, CatagorieAdmin)
admin.site.register(SubCatagorie, SubCatagorieAdmin)
admin.site.register(Seller, CustomUserAdmin)
admin.site.register(Buyer, CustomUserAdmin)
admin.site.register(Ad,AdAdmin)

