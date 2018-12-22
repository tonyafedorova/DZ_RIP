from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from dzrip.forms import Registration
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from dzrip.models import CustomerModel


def first(request):
    data = {
        'bios': [{'name': 'Детсво', 'text': 'Родилась в Великом Новгороде'}, {'name': 'Образование', 'text': 'Художественное образование получила в МГУДТ'}]
    }

    if not request.user.is_authenticated:
        return render(request, 'firstnotlog.html', data)
    else:
        return render(request, 'first.html', data)


def firstnotlog(request):
    data = {
        'bios': [{'name': 'Детсво', 'text': 'Родилась в Великом Новгороде'}, {'name': 'Образование', 'text': 'Художественное образование получила в МГУДТ'}]
    }

    return render(request, 'firstnotlog.html', data)


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_action'] = reverse('login')
        return data

    def get_success_url(self):
        return reverse('root')


def logout(request):
    auth.logout(request)
    if not request.user.is_authenticated:
        return render(request, 'firstnotlog.html')
    else:
        return HttpResponseRedirect(reverse('firstnotlog'))


def pictures(request):
    picture = [
        {
            'pic': 'new-york.jpg',
            'text': 'Нью-Йорк',
            'price': 500
        },
        {
            'text': 'Венеция',
            'price': 600
        },
        {
            'text': 'Фреди',
        },
    ]
    if not request.user.is_authenticated:
        data = {
            'bios': [{'name': 'Детсво', 'text': 'Родилась в Великом Новгороде'},
                     {'name': 'Образование', 'text': 'Художественное образование получила в МГУДТ'}]
        }
        return render(request, 'firstnotlog.html', data)
    else:
        return render(request, 'pictures.html', context={'pictures': picture})


def picturenotlog(request):
    picture = [
        {
            'pic': 'new-york.jpg',
            'text': 'Нью-Йорк',
            'price': 500
        },
        {
            'text': 'Венеция',
            'price': 600
        },
        {
            'text': 'Фреди',
        },
    ]
    return render(request, 'picturenotlog.html', context={'pictures': picture})


class Profile(TemplateView):
    template_name = "Profile.html"

    def get(self, request):
        data1 = CustomerModel.objects.all()
        data2 = {
            'bios': [{'name': 'Детсво', 'text': 'Родилась в Великом Новгороде'},
                     {'name': 'Образование', 'text': 'Художественное образование получила в МГУДТ'}]
        }
        if not request.user.is_authenticated:
            return render(request, 'firstnotlog.html', data2)
        else:
            return render(request, 'Profile.html', context={'data': data1})


class forLab5(TemplateView):
    template_name = "forLab5.html"

    def get(self, request):
        data = CustomerModel.objects.all()
        return render(request, 'forLab5.html', context={'data': data})


def signup(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("root")
    else:
        form = Registration()
        args = {'form': form}
        return render(request, 'signup.html', args)
