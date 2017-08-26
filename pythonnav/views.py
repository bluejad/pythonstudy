# coding:utf-8
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import QuestionCategory, Question, ReplyQuestion, Userphoto, StudyrRecoder
from django.contrib.auth import authenticate, login, logout
import json
from django.http import HttpResponse
import time
import datetime

#key = 'QuestionCache'
#from django.core.cache import cache
# Create your views here.

#主页
def index(request):
    return render(request,'index.html')
#登录
def SIGN_IN_NOW(request):
    return render(request,'login.html')
#注册
def register_html(request):
    return render(request,'register.html')
#学习资源
def buttons_html(request):
    return render(request,'buttons.html')
#技术交流
def blogindex_html(request):
    #获取问题所有分类
    a = QuestionCategory.objects.all()
    es = []
    for e in a:
        es.append(e.category_name)

    # 展示所有的问题
    from django.core.paginator import Paginator
    from django.core.paginator import EmptyPage
    from django.core.paginator import PageNotAnInteger
    limit = 10  # 每页显示的记录条数

    #if cache.has_key(key):
    #    question = cache.get(key)
    #else:
    question = Question.objects.all().order_by('-question_date')
    paginator = Paginator(question,limit)#实例化一个分页对象

    page = request.GET.get('page') #获取到页码

    try:
        q = paginator.page(page) #获取某夜对应的记录
    except PageNotAnInteger: #如果页码不是个整数
        q = paginator.page(1)#取第一页的记录
    except EmptyPage:#如果页码太大
        q = paginator.page(paginator.num_pages)#取最后一页的记录

    #
    if request.user.is_authenticated():
        # 获取用户头像的图片
        imgs = Userphoto.objects.filter(userid=request.user)
        if imgs:
            for img in imgs:
                if img.headImg:#如果用户上传了头像就返回头像
                    return render(request, 'blogindex.html', {'es': es, 'q': q, 'img': img})
                else:#如果用户没上传头像,就把默认用户的头像给用户用
                    imgs = Userphoto.objects.filter(userid=1)
                    for img in imgs:
                        return render(request, 'blogindex.html', {'es': es, 'q': q, 'img': img})
        else:
            return render(request, 'blogindex.html', {'es': es, 'q': q})
    else:
        return redirect('pythonnav:SIGN_IN_NOW')


def questioncontents(request,detail_question_id):
    question = get_object_or_404(Question, id=detail_question_id)

    questionreplys = ReplyQuestion.objects.filter(question_category=question)

    return render(request,'form_validation.html',{'question':question, 'questionreplys':questionreplys})


def calendar_html(request):
    return render(request,'calendar.html')

#我的主页
def profile_html(request):
    if request.user.is_authenticated():

        # 展示所有的问题
        from django.core.paginator import Paginator
        from django.core.paginator import EmptyPage
        from django.core.paginator import PageNotAnInteger

        limit = 5  # 每页显示的记录条数
        question = StudyrRecoder.objects.filter(question_author=request.user.id).order_by('-question_date')
        paginator = Paginator(question, limit)  # 实例化一个分页对象

        page = request.GET.get('page')  # 获取到页码

        try:
            q = paginator.page(page)  # 获取某夜对应的记录
        except PageNotAnInteger:  # 如果页码不是个整数
            q = paginator.page(1)  # 取第一页的记录
        except EmptyPage:  # 如果页码太大
            q = paginator.page(paginator.num_pages)  # 取最后一页的记录

        # 获取用户头像的图片
        imgs = Userphoto.objects.filter(userid=request.user)

        if imgs:
            for img in imgs:
                if img.headImg:#如果用户上传了头像就返回头像
                    return render(request, 'profile.html', {'img': img, 'q': q})
                else:#如果用户没上传头像,就把默认用户的头像给用户用
                    imgs = Userphoto.objects.filter(userid=1)
                    for img in imgs:
                        return render(request, 'profile.html', {'img': img, 'q': q})
        else:
            return render(request, 'profile.html', {'q': q})
    else:
        return redirect('pythonnav:SIGN_IN_NOW')


def ajax_list(request):
    question = Question.objects.all().order_by('-question_date')[:10]
    es = []
    for e in question:
        es.append(e.question_title)
    return HttpResponse(json.dumps(es), content_type='application/json')

#忘记密码
def form_component_html(request):
    return render(request,'form_component.html')







































def user_register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username=username,password=password,email=email)#如果不用create_user,则不会保存hash化的password
    user.save()
    user1 = authenticate(username=username, password=password)
    login(request,user1)
    return redirect('pythonnav:index')

# def login(request):
#     name = request.POST['name']
#     password = request.POST['password']
#     user = authenticate(name, password)
#     if user is not None:
#         if user.is_active:
#             print "User is valid,active and authenticated"
#         else:
#             print "password is valid,but need to active"
#     else:
#         print "the username and password were incorrect"
#使用autjenticate()和login()


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username,password=password)

    if user is not None:
        # if user.is_active:
        login(request,user)
        # print 'succeed'
        # return render(request,'index.html')
        #
        return HttpResponse(1)

    else:
        # es="用户名或者密码错误"
        # return HttpResponse({'var1' : json.dumps(es)}, content_type='application/json')
        return HttpResponse("用户名或者密码错误")


def user_logout(request):
    logout(request)
    return redirect('pythonnav:index')


def change_password():
    u = User.objects.get(username = 'john')
    u.set_password('new password')
    u.save()


def ask_question(request):

    question_category_name = request.POST['radio']
    question_title = request.POST['question_title']
    question_keywords = request.POST['question_keywords']
    question_text = request.POST['question_content']
    #没必要再设置这个字段了,models里面可以用auto_now自动获取当前时间的question_date = datetime.datetime.now()
    question_author = request.user
    joe = QuestionCategory.objects.get(category_name=question_category_name)
    qqqq = Question(question_category=joe,question_title=question_title,question_keywords=question_keywords,question_text=question_text,question_author=question_author)
    qqqq.save()

    #更新缓存
    #cache.set(key, list(Question.objects.all().order_by('-question_date')))

    return redirect('pythonnav:blogindex_html')


def reply_question(request):
    #拿到问题ID,拿到回复内容,然后插入回复表
    question_id = request.POST['question_id']
    question_reply_text = request.POST['question_reply_content']
    question_author = request.user
    question_date = datetime.datetime.now()

    question = get_object_or_404(Question, id=question_id)

    replyqqqq = ReplyQuestion(question_category=question,question_author=question_author,question_date=question_date,question_text=question_reply_text,)

    replyqqqq.save()

    return redirect('pythonnav:blogindex_html')




def uploadImg(request):
    from .models import Userphoto
    if request.method == 'POST':
        Userphoto.objects.filter(userid=request.user).delete()
        new_img = Userphoto(userid=request.user, headImg=request.FILES.get('img'))
        new_img.save()
    return redirect('pythonnav:blogindex_html')

def changepersonalprofile(request):
    username = request.POST['username']
    email = request.POST['email']
    User.objects.filter(id=request.user.id).update(username=username,email=email)
    if request.FILES.get('img') == None:
        pass
    else:
        Userphoto.objects.filter(userid=request.user).delete()
        new_img = Userphoto(userid=request.user, headImg=request.FILES.get('img'))
        new_img.save()
    return redirect('pythonnav:profile_html')


def studyrecoder(request):
    StudyrRecoder.objects.create(question_author=request.user,question_text=request.POST['studyrecoder'])
    return redirect('pythonnav:profile_html')

def sendemail(request):
    emailaddress = request.POST['email']
    if User.objects.filter(email=emailaddress):
        for i in User.objects.filter(email=emailaddress):
            nametemp = i.username
            idtemp = i.id

            # 生成随机密码
            from random import choice
            import string
            # python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
            def GenPassword(length=8, chars=string.ascii_letters + string.digits):
                return ''.join([choice(chars) for i in range(length)])
            pawdtemp = GenPassword(8)

            User.objects.filter(email=emailaddress).delete()
            User.objects.create_user(id=idtemp, username=nametemp, password=pawdtemp,email=emailaddress)

            from django.core.mail import send_mail
            send_mail(
                subject=u"这是新的密码,请使用新的密码登录", message=pawdtemp,
                from_email='python_smtp_test@163.com', recipient_list=[emailaddress, ], fail_silently=False,
            )
            return HttpResponse("新的密码已经发到您的邮箱,请去您的邮箱查收并使用新的密码登录,有问题请联系站长")
    else:
        return HttpResponse("您的邮箱的账户注册信息没有找到")
        #
    #
    #
    # from django.core.mail import send_mail
    # StudyrRecoder.objects.create(question_author=request.user, question_text=request.POST['studyrecoder'])
    # return redirect('pythonnav:profile_html')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def test(request):
    Question.objects.all()
    print Question.objects.all()
    print type(Question.objects.all())
    return HttpResponse(Question.objects.all())

def test1(request):
    print list(Question.objects.all())
    print type(list(Question.objects.all()))
    return HttpResponse(list(Question.objects.all()))