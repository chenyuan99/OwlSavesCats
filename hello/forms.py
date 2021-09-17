from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hello.models import Author
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# add event form
class AddPaperForm(forms.Form):
    class Meta:
        model = Author
        fields = ['title', 'abstract', 'publish_time', 'create_time', 'pid']


# add guest
class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['paperclip', 'realname', 'phone', 'email', 'sign']