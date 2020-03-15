from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Article, ArticleCategory
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from PIL import Image
import markdown

from django.views import View


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    # return render(request, 'article/list.html', context)
    return render(request, 'blog/blog.html', context)


def article_create(request):
    if request.method == 'POST':
        new_article_form = ArticlePostForm(request.POST, request.FILES)
        if new_article_form.is_valid():
            new_article = new_article_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            if request.POST['category'] != 'none':
                new_article.category = ArticleCategory.objects.get(id=request.POST['category'])
            new_article.save()
            new_article_form.save_m2m()
            return redirect("article:article_list")
        else:
            return HttpResponse("error")
    else:
        new_article_form = ArticlePostForm()
        categorys = ArticleCategory.objects.all()
        context = { 'article_post_form': new_article_form, 'categorys': categorys }
        return render(request, 'blog/new_blog.html', context)


def article_detail(request, id):
    article = Article.objects.get(id=id)
    article.total_views += 1
    article.save(update_fields=['total_views'])
    article.body = markdown.markdown(article.body,extensions=[
                                'markdown.extensions.extra',
                                'markdown.extensions.codehilite',
                                'markdown.extensions.toc',
                            ])
    context = { 'article':article }
    return render(request, 'blog/blog_detail.html', context)


def article_update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article_form = ArticlePostForm(data=request.POST)
        if article_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.tags.set(*request.POST.get('tags').split(','), clear=True)
            if request.POST['category'] != 'none':
                article.category = ArticleCategory.objects.get(id=request.POST['category'])
            else:
                article.category = None
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            # TODO: Fix popup function
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_form = ArticlePostForm()
        tags = ','.join([tag for tag in article.tags.names()])
        categorys = ArticleCategory.objects.all()
        context = { 'article':article, 'article_form':article_form, 'tags': tags, 'categorys': categorys }
        return render(request, 'blog/update_blog.html', context)


def article_safe_delete(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        article.delete()
        return redirect('article:article_list')
    else:
        return HttpResponse('error')


class likesView(View):
    def post(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs.get('id'))
        article.like += 1
        article.save()
        return HttpResponse('success')
