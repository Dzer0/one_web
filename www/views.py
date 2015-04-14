#coding=utf-8
from django.shortcuts import render,render_to_response,RequestContext,HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password   #引入加密
import models
from django.http import Http404
from models import Members,Comments
from django import  forms
# Create your views here.
import datetime


#注册表单
class regUser(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'UserName','autocomplete':'off','id':'username','autofocus':''}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','autocomplete':'off','id':'inputEmail','required':'','autofocus':''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password','autocomplete':'off'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password','autocomplete':'off'}))


#登陆表单
class loginUser(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


#评论表单
class Commnets_form(forms.Form):
    context = forms.CharField(widget=forms.Textarea())

#首页
def index(req):
    try:
        web = models.WebIntroduction.objects.all()
        lanmu = models.Column.objects.all()
        return render_to_response('index.html',locals())
    except TemplateDoesNotExist:
        raise Http404()

#关于我们
def about(req):
    web = models.WebIntroduction.objects.all()
    lanmu = models.Column.objects.all()
    return render_to_response('about.html',locals())

#使用协议
def terms(req):
    web = models.WebIntroduction.objects.all()
    lanmu = models.Column.objects.all()
    return render_to_response('terms.html',locals())

#栏目
def cate(req,cate_id):
    web = models.WebIntroduction.objects.all()
    lanmu = models.Column.objects.all()
    list = models.Article.objects.filter(column__id=cate_id)
    lanmutitle =models.Column.objects.filter(id=cate_id)
    #cate_list =models.Article.objects.all()
    return render_to_response('list.html',locals(),context_instance=RequestContext(req))

#文章显示
def article(req,art_id):
    sessusername = req.session.get('username','')

#    sessusername = req.session['username']
    web = models.WebIntroduction.objects.all()
    lanmu = models.Column.objects.all()
    context = models.Article.objects.filter(id=art_id)
    comments = models.Comments.objects.filter(article_id=art_id)
    if sessusername =='':
        m =loginUser()
    else:
        pl =Commnets_form()
    return render_to_response('article.html',locals(),context_instance=RequestContext(req))


#用户中心
def  User(req):
    sessusername = req.session.get('username','')
    if sessusername =='':
         return HttpResponse('<script>alert("您未登陆，单击跳转到登陆页面");top.location="/login/";</script>')
    else:
        username = req.session['username']
        web = models.WebIntroduction.objects.all()
        lanmu = models.Column.objects.all()
        ls = models.Members.objects.get(username= username)
        print ls
        #pl = models.Members.objects.get(com_user=id.id)
       # print pl
        return render_to_response('user.html',locals())

#注册用户
def reg_User(req):
    if req.method == 'POST':
        m = regUser(req.POST)
        if m.is_valid():
            username = m.cleaned_data['username']
            email = m.cleaned_data['Email']
            password = m.cleaned_data['password']
            confirm_password = m.cleaned_data['confirm_password']
            print username,email,password,confirm_password
            sha256 =make_password(password,'Dzer0','pbkdf2_sha256')
            md5_pwd = make_password(sha256,None,'unsalted_md5')
            print sha256
            print md5_pwd
            #reg_date = datetime.datetime.now()
            #print reg_date
            #OneEmail = Members.objects.get(email= email)
            #print OneEmail
            if password == confirm_password:

                #print OneEmail

                #if OneEmail:
                #    xxerror = '该邮箱已注册请更改邮箱并重新注册！！！'
                #    render_to_response('reg.html',locals(),context_instance=RequestContext(req))
                Members.objects.create(username=username,passwd=md5_pwd,email=email)
                return HttpResponseRedirect('/login/')
    else:
        m = regUser()
        return render_to_response('reg.html',locals(),context_instance=RequestContext(req))

#用户登录
def login_User(req):
    if req.method =='POST':
        m = loginUser(req.POST)
        if m.is_valid():
            username = m.cleaned_data['username']
            password = m.cleaned_data['password']
            #print username,password
            sha256 =make_password(password,'Dzer0','pbkdf2_sha256')
            md5_pwd = make_password(sha256,None,'unsalted_md5')
            login_static = Members.objects.filter(username=username,passwd=md5_pwd)
            print login_static
            if login_static:
                sessusername = req.session['username'] =username
                print sessusername
                web = models.WebIntroduction.objects.all()
                lanmu = models.Column.objects.all()
                return HttpResponseRedirect('/User/')
                #return render_to_response('user.html',locals(),context_instance=RequestContext(req))
            else:
                return HttpResponse('<script>alert("密码或用户名错误");top.location="/login/";</script>')

            #return HttpResponse('test')
    else:
        web = models.WebIntroduction.objects.all()
        lanmu = models.Column.objects.all()
        m = loginUser()     #将m指向登陆表单
        print m
    #if req.method =='POST':
        #userlogin =
        #error = '<script>alert"sldjflksd";</script>'
        return render_to_response('user.html',locals(),context_instance= RequestContext(req))

#退出登录
def logout_User(req):
    req.session['username']=''
    #return render_to_response('user.html',locals())
    return HttpResponseRedirect('/login/')

#测试评论
def comment_ly(req,art_id):
    if req.method =='POST':
        ly = Commnets_form(req.POST)
        if ly.is_valid():
            context =ly.cleaned_data['context']
            try:
                com_user =Members.objects.get(username = req.session['username'])
            except com_user.DoesNotExist:
                raise Http404
            try:
                article_id = models.Article.objects.get(id =art_id)
            except article_id.DoesNotExist:
                raise Http404
            print context,com_user,article_id
            Comments.objects.create(context =context,com_user=com_user,article_id=article_id)
            return HttpResponse('<script>alert("Success");top.location="/Article/'+art_id+'";</script>')

#评论列表
def User_list(req,user_id):     #评论列表
    sessusername = req.session['username']
    if sessusername =='':
         return HttpResponse('<script>alert("您未登陆，单击跳转到登陆页面");top.location="/login/";</script>')
    else:
        username = req.session['username']
        web = models.WebIntroduction.objects.all()
        lanmu = models.Column.objects.all()
        list_comment = models.Comments.objects.filter(com_user=user_id)
        return render_to_response('user.html',locals())

#评论列表1=======在用此种方式
def User_list1(req,user):
    sessusername = req.session['username']
    if sessusername =='':
         return HttpResponse('<script>alert("您未登陆，单击跳转到登陆页面");top.location="/login/";</script>')
    else:
        lanmu = models.Column.objects.all()
        userid = models.Members.objects.get(username =user)
        list_comment = models.Comments.objects.filter(com_user = userid)
        return render_to_response('user.html',locals(),context_instance=RequestContext(req))

#删除评论

def del_comments(req,comments_id):
    sessusername = req.session['username']
    if sessusername =='':
         return HttpResponse('<script>alert("您未登陆，单击跳转到登陆页面");top.location="/login/";</script>')
    else:
        models.Comments.objects.filter(id = comments_id).delete()
        return HttpResponse('<script>alert("删除成功");window.history.back(-1);</script>')


#根据作者文章列表
def article_list(req,article_user):         #用户文章列表
    lanmu = models.Column.objects.all()
    article_user =article_user
    userid = models.Members.objects.get(username = article_user)
    list = models.Article.objects.filter(author = userid)
    return render_to_response('article_list.html',locals(),context_instance=RequestContext(req))

#读书列表
def Book_list(req):
    lanmu = models.Column.objects.all()
    web = models.WebIntroduction.objects.all()
    book_list = models.Books.objects.all()
    return render_to_response('book_list.html',locals())