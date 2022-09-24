from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Title, Write
from .forms import TitleForm, WriteForm

# Create your views here.

def index(request):
	'''主页'''
	return render(request, 'white_dreams/index.html')

@login_required
def titles(request):
	'''所有主题的页面'''
	titles = Title.objects.filter(owner=request.user).order_by('date_added')
	context = {'titles': titles}
	return render(request, 'white_dreams/titles.html', context)

@login_required
def title(request, title_id):
	'''特定主题的页面'''
	title = Title.objects.get(id=title_id)
	#确认请求的主题属于当前用户
	if title.owner != request.user:
		raise Http404

	writes = title.write_set.order_by('-date_added')
	context = {'title': title, 'writes': writes}
	return render(request, 'white_dreams/title.html', context)

@login_required
def new_title(request):
	'''添加主题的页面'''
	if request.method != 'POST':
		#未提交数据 创建一个新表单
		form = TitleForm()
	else:
		#POST提交的数据 对数据进行处理
		form = TitleForm(data=request.POST)
		if form.is_valid():
			new_title = form.save(commit=False)
			new_title.owner = request.user
			new_title.save()
			return redirect('white_dreams:titles')

	#显示空表单或指出表单数据无效
	context = {'form': form}
	return render(request, 'white_dreams/new_title.html', context)

@login_required
def new_write(request, title_id):
	'''添加内容的页面'''
	title = Title.objects.get(id=title_id)

	if request.method != 'POST':
		#未提交数据 创建新表单
		form = WriteForm()
	else:
		#POST交的数据 对数据进行处理
		form = WriteForm(data=request.POST)
		if form.is_valid():
			new_write = form.save(commit=False)
			new_write.title = title
			new_write.save()
			return redirect('white_dreams:title', title_id=title_id)

	#显示空表单或指出表单数据无效
	context = {'title': title, 'form': form}
	return render(request, 'white_dreams/new_write.html', context)	
