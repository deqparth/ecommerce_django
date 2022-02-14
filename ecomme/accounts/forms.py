from django import forms


# from . import allauth 
from allauth.account.forms import SignupForm 



from . models import MyUser 
class MySignupForm(SignupForm):
    genderchoices = [
        ("M", "Male"),
        ("F", "Female")
    ]
    full_name = forms.CharField(max_length=30, label='full_name')
    address = forms.CharField(max_length=30, label='address')
    date_of_birth = forms.DateField(label = 'date_of_birth',widget=forms.SelectDateWidget,)
    gender = forms.ChoiceField( choices=genderchoices)

    class Meta:
        model = MyUser

    
    def save(self, request):
         
        user = super().save(request)
        user.full_name = self.cleaned_data['full_name']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.save()
        print(user)
        return user