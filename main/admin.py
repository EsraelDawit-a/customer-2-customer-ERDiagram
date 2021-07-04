from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as A
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','contac_info','Adress','optional_adress','first_name','last_name','role' ]
    #
class ProfileAdmin(admin.ModelAdmin):
   list_display =  ['user','user_picture','bio']

class MainCatagorieAdmin(admin.ModelAdmin):
    list_display = ['catagorie_name','created_date','catagorie_decription']

class SubCatagorieAdmin(admin.ModelAdmin):
    list_display = ['sub_catagorie_name','created_date','sub_catagorie_decription']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile,ProfileAdmin)

admin.site.register(MainCatagorie,MainCatagorieAdmin)
admin.site.register(SubCatagorie,SubCatagorieAdmin)
