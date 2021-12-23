from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

from articles.models import Article


def my_response(request):

    random_database_id = random.randint(1, 3)
    article_obj = Article.objects.get(id=random_database_id)


    title = f"<h1>{article_obj.title}______({article_obj.id})</h1>"
    content = f"<p>{article_obj.content}</p>"

    html_string = title + content
    return HttpResponse(html_string)
