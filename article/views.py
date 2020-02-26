from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


def article_create(request):
    return HttpResponse('this is article create page')


def article_detail(request, id):
    article = Article.objects.get(id=id)
    context = { 'article':article }
    return render(request, 'article/detail.html', context)


def article_update(request):
    return HttpResponse('this is article update page')


def article_delete(request):
    return HttpResponse('this is article delete page')
