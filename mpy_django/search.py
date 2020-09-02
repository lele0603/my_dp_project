# coding=utf8
from django.http import HttpResponse
from django.shortcuts import render

# 表单


def search_form(request):
    return render(request, 'search_form.html')


# 接手请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '您搜索的内容是：' + request.GET['q']
    else:
        message = '您搜索内容为空'
    return HttpResponse(message)
