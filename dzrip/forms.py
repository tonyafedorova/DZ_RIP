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


# class PictureCreationForm(ModelForm):
#     class Meta:
#         model = Picture
#         fields = ['name', 'description', 'price', 'author', 'image']
#
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user')
#         super().__init__(*args, **kwargs)
#         self.user = user
#         for field in self.fields.values():
#             field.widget.attrs.update({'class': 'form-control'})
#
#     def save(self, commit=True):
#         pic = super().save(commit=False)
#         if commit:
#             pic.save()
#         pic.executor.set([self.user])
#         return pic


class PictureCreateForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'description', 'author', 'price', 'image']

    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.user = user
    #     for field in self.fields.values():
    #         field.widget.attrs.update({'class': 'form-control'})
    #
    # def save(self, commit=True):
    #     pic = super().save(commit=False)
    #     if commit:
    #         pic.save()
    #     pic.executor.set([self.user])
    #     return pic