from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from dzrip.forms import Registration, PictureCreateForm, PictureCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from dzrip.forms import Edit
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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


def pictures(request):
    # args = {"pic": request.pic}

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


class PictureListView(LoginRequiredMixin, ListView):
    model = Picture
    template_name = 'pictures.html'
    context_object_name = "pictures"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        data['form_create'] = PictureCreateForm(self.request.user)
        return data

    def get_queryset(self):
        if self.kwargs['whose'] == 'my':
            return self.model.objects.filter(executor=self.request.user.id).order_by('id')
        if self.kwargs['whose'] == 'all':
            return self.model.objects.all().order_by('id')


class PictureView(LoginRequiredMixin, TemplateView):
    template_name = 'picture.html'

    def get_context_data(self, id, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        data['is_executor'] = False
        data['last_executor'] = False
        pic_exec = Picture.objects.get(id=id).executor
        cur_user = pic_exec.filter(id=user.id)
        if cur_user.exists():
            data['is_executor'] = True
            if pic_exec.all().count() == 1:
                data['last_executor'] = True
        data['picture'] = Picture.objects.get(id=id)
        return data


class PictureCreateView(LoginRequiredMixin, CreateView):
    form_class = PictureCreationForm
    template_name = 'picture_creation.html'
    model = Picture

    def get_success_url(self):
        return reverse('picture_list', kwargs={'whose': 'my'})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PictureRemoveView(LoginRequiredMixin, DeleteView):
    def get(self, request, id, **kwargs):
        Picture.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('picture_list', kwargs={'whose': 'my'}))


class PictureListPageView(ListView):
    model = Picture
    template_name = 'picture_page.html'
    context_object_name = "pictures"
    paginate_by = 5

    def get_queryset(self):
        if self.kwargs['whose'] == 'my':
            return Picture.objects.filter(executor=self.request.user.id).order_by('id')
        if self.kwargs['whose'] == 'all':
            return Picture.objects.all().order_by('id')


class FastPictureCreateView(LoginRequiredMixin, CreateView):
    form_class = PictureCreationForm
    template_name = 'picture_element.html'
    model = Picture
    #fields = ['name', 'description', 'competition_date', 'task_image']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['element'] = Picture.objects.order_by('-id')[0]
        return data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Pics(TemplateView):
    template_name = "pics.html"

    def get(self, request):
        data = Picture.objects.all()
        return render(request, 'pics.html', context={'data': data})