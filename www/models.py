#coding=utf-8
from django.db import models
import datetime
# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

#class Article(models.Model):
#    '''日志'''
#    title = models.CharField(verbose_name='标题', max_length=150, blank=False, null=False)
#    content = RichTextField('正文') # 使用ckeditor中的RichTextField



#用户
class Members(models.Model):
    username = models.CharField(max_length=30)
    passwd = models.CharField(max_length=128)
    email = models.EmailField()
    reg_date = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.username


#栏目
class Column(models.Model):
    name = models.CharField(max_length=30)
    describe = models.TextField()

    def __unicode__(self):
        return self.name


#文章
class Article(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(Members)
    context =RichTextField('内容')
    date = models.DateTimeField(default=datetime.datetime.now())
    column = models.ManyToManyField(Column)

    def __unicode__(self):
        return self.title


#网站标题
class WebIntroduction(models.Model):
    webtitle = models.CharField(max_length=200)
    Copyright = models.TextField(max_length=500)
    About = RichTextField('关于我们')
    Terms = models.TextField(max_length=2000)

    def __unicode__(self):
        return self.webtitle

#留言评论
class Comments(models.Model):
    context =models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now())
    com_user = models.ForeignKey(Members)
    article_id = models.ForeignKey(Article)

    def __unicode__(self):
        return self.context

#在读书籍
class Books(models.Model):
    book_name = models.CharField(max_length=150)
    book_author = models.CharField(max_length=50)
    book_img = models.CharField(max_length=150)
    book_describe = RichTextField('书的描述')
    book_source = models.URLField()
    book_support = models.CharField(max_length=20)
    book_static = models.TextField(max_length=150)

    def __unicode__(self):
        return self.book_name