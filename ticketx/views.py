# Create your views here.
# coding=utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from ticketx.models import User

def register(request):
	if request.method == 'POST':
		userName = request.POST['name'] 			#获取页面中输入的信息
		passWord = request.POST['password'] 		#获取页面中输入的信息
		user = User(name = userName, password = passWord)
		user.save()									#保存进数据库
		return render_to_response("dashboard.html", {"user": user}) #登陆成功
	return render_to_response("register.html", context_instance=RequestContext(request))

def index(request):
	print("login" + request.method)
	if request.method == 'POST':
		# 点击注册
		if 'register' in request.POST:
			return HttpResponseRedirect("./register");
		# 点击登陆
		else:
			userName = request.POST['name']			#获取页面中输入的信息
			passWord = request.POST['password']		#获取页面中输入的信息
			try:
				user = User.objects.get(name = userName) # 从数据库里面查找对应用户名的user
				if user.password != passWord:
					return render_to_response("login_failed.html", {"msg": "用户名或者密码错误!"})
			except ObjectDoesNotExist:
				return render_to_response("login_failed.html", {"msg": "还没有注册哦！"})
			return render_to_response("dashboard.html", {"user": user})
	print("not post")
	return render_to_response('index.html', context_instance = RequestContext(request)) 
