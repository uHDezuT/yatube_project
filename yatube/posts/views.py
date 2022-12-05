from django.http import HttpResponse
from django.shortcuts import render


# Главная страница
def index(request):
    template = '../templates/posts/index.html'
    return render(request, template)


def group_posts(request, slug):
    template = '../templates/posts/group_list.html'
    return render(request, template)
