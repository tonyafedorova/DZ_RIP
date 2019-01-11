from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from dzrip.forms import Registration, PictureCreateForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from dzrip.forms import Edit
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from dzrip.models import customer, Picture


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


def signup(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("root")
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('root'))
            else:
                return redirect('/signup/')
        return redirect('/signup/')
    else:
        form = Registration()
        args = {'form': form}
        return render(request, 'signup.html', args)


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_action'] = reverse('login')
        return data

    def get_success_url(self):
        return reverse('profile')


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


def profedit(request):
    user = request.user
    if request.method=='POST':
        form = Edit(request.POST, request.FILES, instance=request.user)
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


def PictureCreateView(request):
    if request.method == 'POST':
        form = PictureCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PictureCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'picture_creation.html', context)


class Pics(TemplateView):
    template_name = "pics.html"

    def get(self, request):
        data = Picture.objects.all()
        return render(request, 'pics.html', context={'data': data})



def like_post(request):
    post = get_object_or_404(Picture, id=request.POST.get('post_id'))
    # post = get_object_or_404(Picture, id=request.POST.get('id'))
    is_laked = False
    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
        is_laked = False
    else:
        post.like.add(request.user)
        is_laked = True
    return HttpResponseRedirect(reverse('pics'))
    # context = {'data': post}
    # if request.is_ajax():
    #     html = render_to_string('pics.html', context, request=request)
    #     return JsonResponse({'form': html})
