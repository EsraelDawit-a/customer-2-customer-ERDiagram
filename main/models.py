from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


user_roles = (
    ('seller','seller'),
    ('buyer','buyer')
)


''' Common Fields for all Users '''
class CustomUser(AbstractUser):

    ''' Django by Default has username, password, and email-adress Fields '''
    contac_info = models.CharField(max_length=100)
    registerddate = models.DateTimeField(auto_now_add = True)
    role = models.CharField(choices=user_roles,max_length=100,default='empty',null=True,blank=True)
    phone_number_vertified = models.BooleanField(default=False)
    email_adress_vertified = models.BooleanField(default=False)
    Adress = models.CharField(max_length=200,null=True,blank =True)

    ''' if seller us another optional residence or adress'''
    optional_adress = models.CharField(max_length=200,null=True,blank=True)
    is_premium_account = models.BooleanField(default=False)

''' User Profile '''
class Profile(models.Model):
     user = models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE,related_name ='profile')
     user_picture = models.ImageField(upload_to = 'images', default='media/images/app4.jpg', blank =True,null = True)
     bio = models.TextField(null=True,blank=True)

     user_id_image = models.FileField(upload_to = 'media/docimages',blank =True,null = True)
     
     
     def __str__(self):
          return self.user.username


'''Adds Main Catagories'''
class MainCatagorie(models.Model):
    catagorie_name = models.CharField(max_length=100)
    catagorie_decription = models.TextField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=False)
    subcatagory = models.ForeignKey('SubCatagorie',on_delete=models.CASCADE,related_name='sub_catagorie')
    
    #todo display subcatagory in admin

    def __str__(self):
        return self.catagorie_name

''' Adds Sub Catagories'''
class SubCatagorie(models.Model):
    sub_catagorie_name = models.CharField(max_length=100)
    sub_catagorie_decription = models.TextField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.sub_catagorie_name
