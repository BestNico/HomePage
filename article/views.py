from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Article
from .forms import ArticlePostForm
from django.contrib.auth.models import User


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    # return render(request, 'article/list.html', context)
    return render(request, 'blog/blog.html', context)


def article_create(request):
    if request.method == 'POST':
        new_article_form = ArticlePostForm(data=request.POST)
        if new_article_form.is_valid():
            new_article = new_article_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("error")
    else:
        new_article_form = ArticlePostForm()
        context = { 'article_post_form': new_article_form }
        return render(request, 'blog/new_blog.html', context)


def article_detail(request, id):
    article = Article.objects.get(id=id)
    context = { 'article':article }
    return render(request, 'blog/blog_detail.html', context)


def article_update(request):
    return HttpResponse('this is article update page')


def article_safe_delete(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        article.delete()
        return redirect('article:article_list')
    else:
        return HttpResponse('error')
