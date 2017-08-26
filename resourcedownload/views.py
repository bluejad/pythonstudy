#coding:utf-8
from django.shortcuts import render
from .models import downloadstation, Querystation

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# Create your views here.

def dynamic_table_html(request):
    limit = 15  # 每页显示的记录条数
    question = downloadstation.objects.all().order_by('-stationaddtime')
    paginator = Paginator(question, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取到页码

    try:
        q = paginator.page(page) #获取某夜对应的记录
    except PageNotAnInteger: #如果页码不是个整数
        q = paginator.page(1)#取第一页的记录
    except EmptyPage:#如果页码太大
        q = paginator.page(paginator.num_pages)#取最后一页的记录

    return render(request,'resourcedownload/dynamic_table.html',{'q':q})


def querystation_html(request):
    # 展示所有的查询站
    limit = 15  # 每页显示的记录条数
    question = Querystation.objects.all().order_by('-stationaddtime')
    paginator = Paginator(question, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取到页码

    try:
        q = paginator.page(page) #获取某夜对应的记录
    except PageNotAnInteger: #如果页码不是个整数
        q = paginator.page(1)#取第一页的记录
    except EmptyPage:#如果页码太大
        q = paginator.page(paginator.num_pages)#取最后一页的记录

    return render(request,'resourcedownload/querystation.html',{'q':q})