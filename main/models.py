from typing import overload
from django.db import models
from django.contrib.auth.models import AbstractUser

from main.db_fields import ListField
# Create your models here.


# user_roles = (
#     ('seller','seller'),
#     ('buyer','buyer')
# )

class Adress(models.Model):
    state = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)

    class Meta:
        abstract = True

''' Common Fields for all Users '''
class CustomUser(AbstractUser, Adress):

    ''' Django by Default has username, password, and email-adress Fields '''
    contac_info = models.CharField(max_length=100)
    registerddate = models.DateTimeField(auto_now_add = True)
    # role = models.CharField(choices=user_roles,max_length=100,default='empty',null=True,blank=True)
    phone_number_vertified = models.BooleanField(default=False)
    email_adress_vertified = models.BooleanField(default=False)
    user_picture = models.ImageField(upload_to = 'images', default='media/images/app4.jpg', blank =True,null = True)
    user_id_image = models.FileField(upload_to = 'media/docimages',blank =True,null = True)
    bio = models.TextField(null=True,blank=True)

    ''' if seller us another optional residence or adress'''
    optional_adress = models.CharField(max_length=200,null=True,blank=True)
    is_premium_account = models.BooleanField(default=False)






class Seller(CustomUser):
    class Meta:
        verbose_name = 'Seller'

class Buyer(CustomUser):
    class Meta:
        verbose_name = 'Buyer'



'''Adds Main Catagories'''
class Catagorie(models.Model):
    name = models.CharField(max_length=100)
    decription = models.TextField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

''' Adds Sub Catagories'''
class SubCatagorie(models.Model):
    catagorie = models.ForeignKey(Catagorie,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    decription = models.TextField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
    
    fields = ListField(help_text='comma separated value to store list of attributes ad must contain. '
                                 'Ex brand, color, size')

    def __str__(self):
        return self.name


class AdAdress(models.Model):
    state = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)

    class Meta:
        abstract = True

class Ad(AdAdress):
    sub_catagorie = models.ForeignKey(SubCatagorie,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image  = models.ImageField(upload_to = 'media/product_images')
    file_attachment = models.FileField(upload_to = 'media/product_files',null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return self.name




'''order by_data by giving fields given sub catagories by brand,color,size ...'''
def order_by_data(q, reverse=False):
    return Ad.objects.order_by(f"{'-' if reverse else ''}data__{q}")

'''order by_location by giving state ,area or city and order reverse it or normal way'''
def order_by_location(q,reverse=False):
    return Ad.objects.order_by(f"{'-' if reverse else ''}{q}")
  