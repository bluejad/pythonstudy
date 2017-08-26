#coding:utf-8
from django.db import models

# Create your models here.

class downloadstation(models.Model):
    stationaddr = models.CharField(u'网址',max_length=100)
    stationcontent = models.CharField(u'网站内容',max_length=200)
    stationaddtime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.stationcontent

    class Meta:
        verbose_name = '下载站'
        verbose_name_plural = '下载站'
        ordering = ['stationaddtime']

class Querystation(models.Model):
    stationaddr = models.CharField(u'网址',max_length=100)
    stationintroduce = models.CharField(u'网站简介',max_length=200)
    stationaddtime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.stationintroduce

    class Meta:
        verbose_name = '查询站'
        verbose_name_plural = '查询站'
        ordering = ['stationaddtime']