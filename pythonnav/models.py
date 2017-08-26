#coding:utf-8
from django.db import models

# Create your models here.

class QuestionCategory(models.Model):
    category_name = models.CharField('问题分类',max_length=50)

    def __unicode__(self):
        return self.category_name
    class Meta:
        verbose_name = '问题分类'
        verbose_name_plural = '问题分类'


class Question(models.Model):
    question_category = models.ForeignKey(QuestionCategory,verbose_name="归属分类")
    question_title = models.CharField('标题', max_length=50)
    question_author = models.ForeignKey('auth.User', blank=True, null=True,verbose_name='作者')#外键不能直接写别名
    question_keywords = models.CharField('关键词',max_length=20)
    question_date = models.DateTimeField('发表时间', auto_now=True)
    question_text = models.CharField('正文内容', max_length=200)

    def __unicode__(self):
        return self.question_title

    class Meta:
        verbose_name = '技术问题'
        verbose_name_plural = '技术问题'

class ReplyQuestion(models.Model):
    question_category = models.ForeignKey(Question,verbose_name="归属的问题")
    question_author = models.ForeignKey('auth.User', blank=True, null=True,verbose_name='作者')
    question_date = models.DateTimeField('发表时间')
    question_text = models.CharField('回复的内容', max_length=200)

    def __unicode__(self):
        return self.question_text

    class Meta:
        verbose_name = '问题答复'
        verbose_name_plural = '问题答复'


class Userphoto(models.Model):
    userid = models.ForeignKey('auth.User', blank=False, null=True, verbose_name='用户')
    headImg = models.FileField(upload_to='headImg')

    class Meta:
        verbose_name = '用户头像'
        verbose_name_plural = '用户头像'

class StudyrRecoder(models.Model):
    question_author = models.ForeignKey('auth.User', blank=True, null=True,verbose_name='用户')
    question_date = models.DateTimeField('发表时间', auto_now=True)
    question_text = models.CharField('正文内容', max_length=200)

    class Meta:
        verbose_name = '学习日记'
        verbose_name_plural = '学习日记'