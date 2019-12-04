from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth #导入Django已经做好用户体系
from django.contrib.auth.decorators import login_required #限制某个视图函数必须登录才能访问
'''
# 用到的一个新的类 HttpResponseRedirect，它可以对路径进行重定向，从而将登录成功之后的请求
# 指向/event_manage/目录。
创建 event_manage 函数，用于返回发布会管理 event_manage.html 面页。

'''
# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request,"index.html")
    # 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password) #(3.3.2 引用 Django 认证登录)

        # if username =='admin' and password == 'admin123':
            # return HttpResponse('login success!')

        if user is not None:
            auth.login(request, user) #登录  (3.3.2 引用 Django 认证登录)
            # response.set_cookie('user',username,3600) #添加浏览器cookies（3.2.1节）
            request.session['user'] = username #将session信息记录到浏览器（3.2.2）
            response = HttpResponseRedirect('/event_manage/')
            return response

        else:
            return render(request,'index.html',{'error':'username or password error！'})
    # else:
    #     return render(request,'index.html',{'error':'username or password error!'})

# 发布会管理
@login_required #如果想限制某个视图函数必须登录才能访问,只需要在这个函数的前面加上@login_required 即可
def event_manage(request): #用于返回发布会管理 event_manage.html 面页
    # username = request.COOKIES.get('user', '') #读取浏览器cookies（3.2.1）
    username = request.session.get('user','') #读取浏览器session（3.2.2）
    return render(request,'event_manage.html',{'user':username})
