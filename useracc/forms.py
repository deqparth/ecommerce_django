
from django import forms
from django.forms import ModelForm

from .models import User, Product
from allauth.account.forms import SignupForm, LoginForm


class CustomerSignupForm(SignupForm):
    genderchoices = [
        ("M", "Male"),
        ("F", "Female")
    ]

    full_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(
        label='date_of_birth', widget=forms.SelectDateWidget,)
    gender = forms.ChoiceField(choices=genderchoices)

    def save(self, request):
        user = super(CustomerSignupForm, self).save(request)
        user.role = "customer"
        user.full_name = self.cleaned_data['full_name']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.save()
        return user


class ShopSignupForm(SignupForm):
    genderchoices = [
        ("M", "Male"),
        ("F", "Female")
    ]
    full_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(
        label='date_of_birth', widget=forms.SelectDateWidget,)
    gender = forms.ChoiceField(choices=genderchoices)
    shopname = forms.CharField(max_length=50)
    shopaddress = forms.CharField(max_length=200)
    shopdesc = forms.CharField(max_length=500)
    role = "shopowner"


class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = ["last_login", ]


class RequestResponseForm(forms.Form):
    choices = [
        ("approve", "approve"),
        ("reject", "reject")
    ]

    action = forms.ChoiceField(choices=choices)
    message = forms.CharField(max_length=200)


class AddProduct(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
