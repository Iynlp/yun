from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here

def register(request):
	'''注册用户'''
	if request.method != 'POST':
		#显示空的注册表单
		form = UserCreationForm()
	else:
		#处理填写好的表单
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#让用户自动登入 在重定向到主页
			login(request, new_user)
			return redirect('white_dreams:index')

	#显示空表单或指出表单无效
	context = {'form': form}
	return render(request, 'registration/register.html', context)
