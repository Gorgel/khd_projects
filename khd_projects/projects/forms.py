from django import forms
from models import Project, UserProfile, User, SubCategory, DifficultyLevel

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
    title = forms.CharField(max_length=120, required=True)
    description = forms.CharField(max_length=300, required=False, widget=forms.Textarea())

    class Meta:
        model = Project
        fields = ('category', 'sub_category', 'difficulty_level', 'title', 'description', 'article',  )

class ProjectEditForm(forms.ModelForm):
    article = forms.CharField(max_length=6000, required=False, widget=forms.Textarea())
    title = forms.CharField(max_length=120, required=False)
    description = forms.CharField(max_length=300, required=False, widget=forms.Textarea())

    class Meta:
        model = Project
        fields = ('category', 'sub_category', 'difficulty_level', 'title', 'description', 'article',  )


class CheckboxesForm(forms.Form):
    choices = forms.BooleanField()

class RadioboxForm(forms.Form):
    choices = forms.ChoiceField(widget=forms.RadioSelect())

class CategoryFilterForm(forms.Form):
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all())
    difficulty_level = forms.ModelChoiceField(queryset=DifficultyLevel.objects.all())