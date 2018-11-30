from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView



from django.views import View

from dzrip.models import CustomerModel


def first(request):
    data = {
        'bios': [{'name': 'Childhood', 'text': 'jfkvnvn'}, {'name': 'Education', 'text': 'jfkbhbh'} ]
    }

    return render(request, 'first.html', data)


def firstnotlog(request):
    data = {
        'bios': [{'name': 'Childhood', 'text': 'jfkvnvn'}, {'name': 'Education', 'text': 'jfkbhbh'} ]
    }

    return render(request, 'firstnotlog.html', data)


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
    return render(request, 'pictures.html', context={'pictures': picture})


def bios(request, name):
    data={
        'bio':{
            'name': name,
        }
    }

    return render(request, 'bio.html', data)


class Profile(TemplateView):
    template_name = "Profile.html"

    def get(self, request):
        data = CustomerModel.objects.all()
        return render(request, 'Profile.html', context={'data': data})


class forLab5(TemplateView):
    template_name = "forLab5.html"

    def get(self, request):
        data = CustomerModel.objects.all()
        return render(request, 'forLab5.html', context={'data': data})
