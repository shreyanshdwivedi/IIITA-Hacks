from django import forms
from django.forms import extras

from django.utils.text import slugify

from .models import Product, User

PUBLISH_CHOICES = (
	('publish', "Publish"),
	('draft', "Draft"),
)
GENDER_CHOICES = (
	('male', "Male"),
	('female', "Female"),
)



class ProductModelForm(forms.ModelForm):
	#publish = forms.ChoiceField(choices=PUBLISH_CHOICES, required=False)
	class Meta:
		model = Product
		fields = [
			"title",
			"description",
			"price",
			"discount_percentage"
		]
		widgets = {
			"description": forms.Textarea(
					attrs={
						"placeholder": "New Description",
						'class': 'form-control input-md',
						'name': 'description',
					}
				),
			"title": forms.TextInput(
				attrs= {
					"placeholder": "Title",
					'class': 'form-control input-md',
					'name': 'title',
				}
			),
			"discount_percentage": forms.TextInput(
				attrs={
					"placeholder": "Discount Percentage",
					'class': 'form-control input-md',
					'name': 'discount',
				}
			)
		}

	def clean(self, *args, **kwargs):
		cleaned_data = super(ProductModelForm, self).clean(*args, **kwargs)
		return cleaned_data

	def clean_price(self):
		price = self.cleaned_data.get("price")
		if price <= 20.00:
			raise forms.ValidationError("Price must be greater than INR 25.00")
		elif price >= 100000.00:
			raise forms.ValidationError("Price must be less than INR 50,000.00")
		else:
			return price

	def clean_title(self):
		title = self.cleaned_data.get("title")
		if len(title) > 3:
			return title
		else:
			raise forms.ValidationError("Title must be greater than 3 characters long.")


class RegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
			"name",
			"username",
			"phone",
			"gender",
			"about",
			"email",
			"password",
			"college",
			"date_of_birth",
		]

		widgets = {
			"name": forms.TextInput(

				attrs={
					"placeholder": "Name",
					'class': 'form-control input-md',
					'name': 'name',
				}
			),
			"username": forms.TextInput(
				attrs={
					"placeholder": "Username",
					'class': 'form-control input-md',
					'name': 'username',
				}
			),
			"college": forms.TextInput(
				attrs={
					"placeholder": "College Name",
					'class': 'form-control input-md',
					'name': 'college',
				}
			),
			"phone": forms.TextInput(
				attrs={
					"placeholder": "Contact Number",
					'class': 'form-control input-md',
					'name': 'phone',
				}
			),
			"about": forms.Textarea(
				attrs={
					"placeholder": "About Yourself",
					'id': 'textarea',
					'class': 'form-control',
					'name': 'about',
				}
			),
			"email": forms.TextInput(
				attrs={
					"placeholder": "Email",
					'id': 'inputEmail3',
					'class': 'form-control',
					'name': 'email',
				}
			),
			"password": forms.PasswordInput(
				attrs={
					"placeholder": "Password",
					'id': 'inputPassword3',
					'class': 'form-control',
					'name': 'password',
				}
			),
			"gender": forms.Select(
				attrs = {
					'name' : 'gender'
				}
			),
			"date_of_birth":forms.TextInput(#years = range(1980, 2010),
				attrs={
					'name': 'dob'
					#'class':'datepicker'
				}
			),
		}

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			"username",
			"password",
		]
		widgets = {
			"username": forms.TextInput(
				attrs={
					"placeholder": "Username",
					'class': 'form-control input-md',
					'name': 'username',
				}
			),
			"password": forms.PasswordInput(
				attrs={
					"placeholder": "Password",
					'id': 'inputPassword3',
					'class': 'form-control',
					'name': 'password',
				}
			),
		}
