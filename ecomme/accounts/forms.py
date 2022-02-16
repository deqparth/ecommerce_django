from django import forms

from allauth.account.forms import SignupForm, LoginForm

from .models import MyUser


class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(
            attrs={'class': "form-control input-lg"})
        self.fields['password1'].widget = forms.TextInput(
            attrs={'class': "form-control input-lg", 'placeholder': "sldhk"})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control input-lg'})
        # print(self)
    genderchoices = [
        ("M", "Male"),
        ("F", "Female")
    ]
    roles = [("admin", "admin"), ("shopowner", "shopowner"),
             ("customer", "customer")]
    full_name = forms.CharField(max_length=30, label='full_name', widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'full_name'
        }))
    address = forms.CharField(max_length=30, label='address', widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'full_name'
        }))

    role = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={

            'type': "hidden",
        }))
    date_of_birth = forms.DateField(
        label='date_of_birth', widget=forms.SelectDateWidget,)
    gender = forms.ChoiceField(choices=genderchoices)
    role = forms.ChoiceField(choices=roles)

    class Meta:
        model = MyUser

    def save(self, request):

        user = super().save(request)
        user.full_name = self.cleaned_data['full_name']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.save()
        return user


class MyLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(
            attrs={'class': "form-control input-lg"})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control input-lg'})

    class Meta:
        model = MyUser


class EditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(
            attrs={'class': "form-control input-lg"})
        self.fields['full_name'].widget = forms.TextInput(
            attrs={'class': "form-control input-lg"})
        self.fields['address'].widget = forms.TextInput(
            attrs={'class': "form-control input-lg"})

    class Meta:
        model = MyUser
        fields = [
            "email",
            "full_name",
            "address",
        ]
