from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from dzrip.forms import Registration
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from dzrip.forms import Edit
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from dzrip.models import customer


def first(request):
    data = {
        'bios': [{'name': 'Детство', 'text': 'Родилась в Великом Новгороде'}, {'name': 'Образование', 'text': 'Художественное образование получила в МГУДТ'}]
    }

    if not request.user.is_authenticated:
        return render(request, 'firstnotlog.html', data)
    else:
        return render(request, 'first.html', data)


def firstnotlog(request):
    data = {
        'bios': [{'name': 'Детство', 'text': 'Родилась в Великом Новгороде'}, {'name': 'Образование', 'text': 'Художественное образование получила в МГУДТ'}]
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
    data = {
        'bios': [{'name': 'Детство', 'text': 'Родилась в Великом Новгороде'},
                 {'name': 'Образование', 'text': 'Художественное образование получила в МГУДТ'}]
    }
    if not request.user.is_authenticated:
        return render(request, 'firstnotlog.html', data)
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
            'bios': [{'name': 'Детство', 'text': 'Родилась в Великом Новгороде'},
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


def Profile(request):
    args = {"user": request.user}
    data2 = {
                'bios': [{'name': 'Детство', 'text': 'Родилась в Великом Новгороде'},
                         {'name': 'Образование', 'text': 'Художественное образование получила в МГУДТ'}]
            }
    if not request.user.is_authenticated:
        return render(request, 'firstnotlog.html', data2)
    else:
        return render(request, 'Profile.html', args)


class forLab5(TemplateView):
    template_name = "forLab5.html"

    def get(self, request):
        data = customer.objects.all()
        return render(request, 'forLab5.html', context={'data': data})


def signup(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("root")
        else:
            return redirect('/signup/')
    else:
        form = Registration()
        args = {'form': form}
        return render(request, 'signup.html', args)


def profedit(request):
    user = request.user
    if request.method=='POST':
        form = Edit(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
        else:
            return redirect('/profile/edit/')
    else:
        form = Edit(instance=request.user)
        args = {'form': form}
        return render(request, 'edit.html', args)


def changepass(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('/profile/password/')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'changepass.html', args)
