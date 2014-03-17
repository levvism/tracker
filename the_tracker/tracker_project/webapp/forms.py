from django import forms
from django.contrib.auth.models import User
from webapp.models import UserProfile, Task, Project


MOSCOW_CHOICE = (
    ('M', 'Must'),
    ('S', 'Should'),
    ('C', 'Could'),
    ('W','Would'),
)

PRIORITY_CHOICE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    firstname = forms.CharField(help_text="Please enter first name.", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    lastname = forms.CharField(help_text="Please enter last name.", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))
    email = forms.CharField(help_text="Please enter your email.", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'email'}))
    password = forms.CharField(help_text="Please enter a password.", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
        
class UserProfileForm(forms.ModelForm):

    website = forms.URLField(help_text="Please enter your website.",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'website'}), required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'picture'}), required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the requirement: ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Task'}))
    description = forms.CharField(max_length=128, help_text="Description of the requirement: ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Description'}))
    classification = forms.ChoiceField(help_text="MoSCoW classification of the requirement.", choices=MOSCOW_CHOICE, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'MoSCoW'}))
    priority = forms.ChoiceField(help_text="Priority of the requirement.", choices=PRIORITY_CHOICE, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Priority'}))
    datetime = forms.DateTimeField(help_text="Deadline of requirement", widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder':'YYYY-MM-DD HH:MM'}) )

    class Meta:
        model = Task

        

        
class new_project_form(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter project name ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Project name'}))
    description = forms.CharField(max_length=256, help_text="Please enter project description ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Project description'}))
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Project
        
class EditForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Edit the title of the task: ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}))
    description = forms.CharField(max_length=128, help_text="Edit the description of the task: ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Description'}))
    classification = forms.ChoiceField(help_text=" Edit MoSCoW classification of the requirement.", choices=MOSCOW_CHOICE, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'MoSCoW'}))
    priority = forms.ChoiceField(help_text=" Edit priority of the requirement.", choices=PRIORITY_CHOICE, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Priority'}))
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Task
        
