from django import forms
from django.contrib.auth.models import User
from webapp.models import UserProfile, Task


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

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the requirement: ")
    description = forms.CharField(max_length=128, help_text="Description of the requirement: ")
    classification = forms.CharField(max_length=128, help_text="MoSCoW classification of the requirement.")
    priority = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Task