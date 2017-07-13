from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-er
from django.shortcuts import render


def home(request):
    string = u'<a href="http://www.baidu.com">我在自强学堂学习Django，用它来建网站</a>'
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    List = map(str, range(100))  # 一个长度为100的 List
    return render(request, 'templates_demo/home.html', {'string': string,'TutorialList': TutorialList,'info_dict':info_dict,'List': List})
