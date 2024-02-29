from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def origin(request):
    if request.method == 'GET':
        return render(request,'index.html')
    name = request.POST.get('Name')
    email = request.POST.get('Email')
    age = request.POST.get('Age')
    message = request.POST.get('Message')
    models.UserMessage.objects.create(name=name,email=email,age=age,message=message)
    return redirect('submit/suscess/')

def info_list(request):
    data_list = models.UserMessage.objects.all()
    return render(request,'info_list.html',{'data_list':data_list})

def submit_suscess(request):
    data = models.UserMessage.objects.last()
    return render(request,'submit_suscess.html',{"data":data})

def info_delete(request):
    id = request.GET.get('nid')
    models.UserMessage.objects.filter(id=id).delete()
    return redirect('/info/list')

def archive_list(request):
    return render(request,'archive_list.html')

def archive_list_2(request):
    return render(request,'archive_list_2.html')

def archive_24_02_27(request):
    return render(request,'凤栖梧桐：记鹏城第一峰登顶.html')

def archive_23_12_11(request):
    return render(request,'2023年终总结.html')

def archive_23_11_23(request):
    return render(request,'一只猫的记忆.html')

def archive_23_11_20(request):
    return render(request,'Robocopy迁移hexo文件保证博客更新时间不变.html')

def archive_23_11_17(request):
    return render(request,'WSL中Rstudio-server调用mamba虚拟环境中的R.html')

def archive_23_11_13(request):
    return render(request,'电脑装机必备软件列表.html')

def archive_23_11_09(request):
    return render(request,'使用wget同时下载多个连续文件.html')

def archive_23_11_02(request):
    return render(request,'随笔杂谈.html')

def archive_23_10_30(request):
    return render(request,'于万米高空读《我与地坛》.html')

def archive_23_10_16(request):
    return render(request,'我和我的朋友们.html')

def archive_23_10_15(request):
    return render(request,'UKBiobank数据提取.html')

def archive_23_02_28(request):
    return render(request,'Autodock对接结果分析.html')

def archive_23_02_23_A(request):
    return render(request,'Autodock分子对接.html')

def archive_23_02_23_D(request):
    return render(request,'Discovery Studio分子对接.html')

def  archive_23_02_20(request):
    return render(request,'考研篇.html')

def archive_23_02_16(request):
    return render(request,'回忆录（一）城市篇.html')