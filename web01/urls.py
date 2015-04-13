#coding=utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from www.views import *
from django.conf import settings  # 引用settings配置文件 为配置富文本需要



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')), # 引入ckeditor
    url(r'^$',index),
    url(r'^About/$',about),
    url(r'^terms/$',terms),
    url(r'^category/(\d+)/$',cate),
    url(r'^Article/(\d+)/$',article),
    url(r'^User/$',User),
    #url(r'^User/(\d+)/$',User_list),
    url(r'^User/(\w+)/$',User_list1),
    url(r'^list/(\w+)/$',article_list),
    url(r'^reg/$',reg_User),
    url(r'^logout/$',logout_User),
    url(r'^login/$',login_User),
    url(r'^comment/(\d+)/$',comment_ly),
    url(r'^User/del/(\d+)/$',del_comments),
    url(r'^Book_list/',Book_list),   

)
