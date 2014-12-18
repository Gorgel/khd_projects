from django import forms
from models import Project, UserProfile, User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    description = forms.CharField(max_length=500, required=False, widget=forms.Textarea())

    class Meta:
        model = UserProfile
        fields = ('picture', 'description')

class ProjectForm(forms.ModelForm):
    article = forms.CharField(max_length=6000, required=False, widget=forms.Textarea())
    title = forms.CharField(max_length=120)
    description = forms.CharField(max_length=300, required=False, widget=forms.Textarea())

    class Meta:
        model = Project
        fields = ('article', 'title', 'description', 'category',)



