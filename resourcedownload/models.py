#coding:utf-8
from django.db import models

# 定义本类为抽象基类，减少冗余代码
class stationBase(models.Model):
    stationaddr = models.CharField(u'网址', max_length=100)
    stationaddtime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class downloadstation(stationBase):
    stationcontent = models.CharField(u'网站内容',max_length=200)

    def __unicode__(self):
        return self.stationcontent

    class Meta:
        verbose_name = '下载站'
        verbose_name_plural = '下载站'
        ordering = ['stationaddtime']

class Querystation(stationBase):
    stationintroduce = models.CharField(u'网站简介',max_length=200)

    def __unicode__(self):
        return self.stationintroduce

    class Meta:
        verbose_name = '查询站'
        verbose_name_plural = '查询站'
        ordering = ['stationaddtime']