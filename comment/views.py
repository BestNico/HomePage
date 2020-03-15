from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from article.models import Article
from .models import Comment
from .forms import CommentForm


def post_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = comment_form.cleaned_data.get('user')
            new_comment.mail = comment_form.cleaned_data.get('mail')
            new_comment.message = comment_form.cleaned_data.get('message')
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        return HttpResponse("发表评论仅接受POST请求。")
