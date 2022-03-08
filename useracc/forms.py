
from django import forms

from .models import User
from allauth.account.forms import SignupForm, LoginForm


class AdminUserUpdateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    full_name = forms.CharField(max_length=50)


class CustomerSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    genderchoices = [
        ("M", "Male"),
        ("F", "Female")
    ]

    full_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(
        label='date_of_birth', widget=forms.SelectDateWidget,)
    gender = forms.ChoiceField(choices=genderchoices)
    role = 'customer'

    class Meta:
        model = User

    # def save(self, request):
    #     user = User()
    #     user.role = "customer"
    #     user.email = self.cleaned_data['email']
    #     # user.set_password(user.password)
    #     user.full_name = self.cleaned_data['full_name']
    #     user.address = self.cleaned_data['address']
    #     user.gender = self.cleaned_data['gender']
    #     user.date_of_birth = self.cleaned_data['date_of_birth']
    #     user.save()
    #     return user

    # Disabled the .save() function because of inherited method SignupForm


class ShopSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    genderchoices = [
        ("M", "Male"),
        ("F", "Female")
    ]
    full_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(
        label='date_of_birth', widget=forms.SelectDateWidget)
    gender = forms.ChoiceField(choices=genderchoices)
    shopname = forms.CharField(max_length=50)
    shopaddress = forms.CharField(max_length=200)
    shopdesc = forms.CharField(max_length=500)
    role = "shopowner"

    class Meta:
        model = User


class AddUserForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
    role = forms.CharField(max_length=50)

    class Meta:
        model = User


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User


class RequestResponseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    choices = [
        ("approve", "approve"),
        ("reject", "reject")
    ]

    class Meta:
        model = User
        fields = []

    response = forms.ChoiceField(choices=choices)


# class AddShop(forms.Form):
#     name = forms.CharField()
#     price = forms.IntegerField()
#     categories = (("electronics", "electronics"), ("footwear",
#                   "footwear"), ("accesories", "accesories"))
#     category = forms.ChoiceField(choices=categories)
#     description = forms.CharField()
#     image = forms.ImageField()
#     brand = forms.CharField()
#     quantity = forms.IntegerField()


class AddProduct(forms.Form):
    categories = (
        ("electronics", "electronics"), ("footwear", "footwear"),
        ("accesories", "accesories")
    )
    name = forms.CharField()
    price = forms.IntegerField()
    category = forms.ChoiceField(choices=categories)
    description = forms.CharField()
    image = forms.ImageField()
    brand = forms.CharField()
    quantity = forms.IntegerField()
