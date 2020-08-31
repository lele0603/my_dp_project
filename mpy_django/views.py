# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello My Django")


def runoob(request):
    # context = {}
    # context['hello'] = "Hello World!"
    # return render(request, 'runoob.html', context)

    # string
    # views_name = "Django 启程"
    # return render(request, "runoob.html", {"name": views_name})

    # list
    # <p>{{ views_list }}</p>   # 取出整个列表
    # <p>{{ views_list.0 }}</p> # 取出列表的第一个元素
    # views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    # return render(request, "runoob.html", {"views_list": views_list})

    # dic
    # <p>{{ views_dict }}</p>
    # <p>{{ views_dict.name }}</p>
    # views_dict = {"name": "菜鸟教程"}
    # return render(request, "runoob.html", {"views_dict": views_dict})

    # filter{{ 变量名 | 过滤器：可选参数 }}--在变量为显示前修改它
    # name = 0
    # return render(request, "runoob.html", {"name": name})

    # name = "开启Django, so easy!!!"
    # return render(request, "runoob.html", {"name": name})

    # num = 1024
    # return render(request, "runoob.html", {"num": num})

    # import datetime
    # now = datetime.datetime.now()
    # return render(request, "runoob.html", {"time": now})

    # {{ views_str|safe }}不转义views_str的值
    # views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    # return render(request, "runoob.html", {"views_str": views_str})

    # <p>{% if num > 90 and num <= 100%}</p>
    # Wonderful!
    # {% elif num > 60 and num <= 90%}
    # Good!
    # {% else %}
    # Bad~
    # {% endif %}
    # views_num = 88
    # return render(request, "runoob.html", {"num": views_num})

    # views_dict = {"course": "Django", "lesson_num": 1}
    # return render(request, "runoob.html", {"views_dict": views_dict})

    # views_list = ["a", "b", "c", "d", "e"]
    # # {% empty%}学习
    # athlete_list = {"athlete": "LiNing", "sports_played": "Gymnastics"}
    #views_list = []
    name = "Django Course"
    return render(request, "runoob.html", {"name": name})
