from django import forms
from django.contrib.auth.models import User
from webapp.models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    firstname = forms.CharField(help_text="Please enter first name.")
    lastname = forms.CharField(help_text="Please enter last name.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
        
class UserProfileForm(forms.ModelForm):

    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
