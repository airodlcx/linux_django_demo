"""linux_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import books.views as books_view
import clac.views as clac_views
import learn.views as learn_views
import templates_demo.views as template_views
import blog.views as blog_views


admin.autodiscover()

urlpatterns = [
    # url(r'^$',clac_views.index),
    url(r'^admin/', admin.site.urls),
    # url(r'^add/$',clac_views.add,name='add'),
    # url(r'^new_add/(\d+)/(\d+)/$',clac_views.add2,name='add2'),
    # url(r'^add/(\d+)/(\d+)/$',clac_views.old_add2_redirect)

    # url(r'^$',learn_views.home,name='home')
    url(r'^blog_home/$', blog_views.index),
    url(r'^blog_columns/$', blog_views.columns),
    url(r'^$',template_views.home,name='home')

]
