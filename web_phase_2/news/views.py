from django.core.serializers import json
from django.shortcuts import render

# Create your views here.
from news.models import News
from django.http import HttpResponse
from django.core import serializers


def get_news_by_id(request, url):
    news = serializers.serialize('json', [News.objects.get(url=url)],
                                 fields=('title', 'date', 'image', 'text', 'field')
                                 )
    return HttpResponse(news)


def get_all_news(request):
    all_news = serializers.serialize('json', News.objects.all(),
                                     fields=('title', 'date', 'image', 'text', 'field')
                                     )
    return HttpResponse(all_news)
