from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.text import slugify

####

GENDER_CHOICES = (
	('male', "Male"),
	('female', "Female"),
)

#### Create your models here.

# def content_file_name(instance, filename):
#     return '/'.join([instance.user.username, filename])

class User(models.Model):
	name = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	college = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length = 12)
	gender = models.CharField(max_length = 6, default = 'male', choices =  GENDER_CHOICES)
	about = models.TextField()
	email = models.EmailField()
	password = models.CharField(max_length = 20)
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
	#image = models.FileField(upload_to= content_file_name, default=content_file_name)


class Product(models.Model):
	#user = models.ForeignKey(User)
	category = models.CharField(max_length=25, blank=True)
	title = models.CharField(max_length = 25)
	slug = models.SlugField(blank = True)
	description = models.TextField(null = True, default = "Descriptions are overrated.")
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 100)
	discount_percentage = models.IntegerField(default=0)
	discount_status = models.BooleanField(default=False)

	media = models.FileField(upload_to='images/%Y/%m/%d/', default='images/%Y/%m/%d/')

	def get_discounted_price(self):
		if self.discount_status:
			return ((100 - discount_percentage) * self.price) / 100.0
		return  self.price


	def __unicode__(self):
		return self.title

def create_slug(instance, new_slug = None):
	slug = slugify(instance.title)
	


class ProductRating(models.Model):
	user = models.ForeignKey(User)
	product = models.ForeignKey(Product)
	rating = models.IntegerField(null=True, blank=True)
	verified = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s" %(self.rating)
