from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from dzrip.models import customer


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


class newpics(UserChangeForm):
    class Meta:
        model = customer
        fields = (
            "picname",
            "picture",
            "description"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        pic = super(newpics, self).save(commit=False)
        pic.picname = self.cleaned_data["picname"]
        pic.picture = self.cleaned_data["picture"]
        pic.description = self.cleaned_data["description"]

        if commit:
            pic.save()

        return pic

