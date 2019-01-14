from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.forms import ModelForm

from dzrip.models import customer, Picture


class Registration(UserCreationForm):
    class Meta:
        model = customer
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super(Registration, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()

        return user


class Edit(UserChangeForm):
    class Meta:
        model = customer
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "description"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super(Edit, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.avatar = self.cleaned_data["avatar"]
        user.description = self.cleaned_data["description"]

        if commit:
            user.save()

        return user


class PictureCreateForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'description', 'author', 'price', 'image']





