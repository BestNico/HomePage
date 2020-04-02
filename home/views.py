from django.shortcuts import render
from article.models import Article
import markdown


def home_page(request):
    blog_list = Article.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'homepage.html', context)

def home_blog_detail(request, id):
    blog = Article.objects.get(id=id)
    blog.body = markdown.markdown(blog.body,extensions=[
                                'markdown.extensions.extra',
                                'markdown.extensions.codehilite',
                                'markdown.extensions.toc',
                            ])
    context = {'blog':blog}
    return render(request, 'homepage_detail.html', context)

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
