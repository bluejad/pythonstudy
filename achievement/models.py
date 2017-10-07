#coding:utf-8
from django.db import models

# 定义本类为抽象基类，减少冗余代码
class AchievementBase(models.Model):
    achievement_author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')  # 外键不能直接写别名

    class Meta:
        abstract = True

# Create your models here.
class AchievementYear(AchievementBase):
    achievement_date = models.CharField(max_length=8, verbose_name='成就年')
    achievement_summary = models.CharField('成就年总结', blank=True, null=True, max_length=50)

    def __unicode__(self):
        return self.achievement_date
    class Meta:
        verbose_name = '成就年'
        verbose_name_plural = '成就年'

class Achievement(AchievementBase):
    achievement_date = models.DateField('发表时间', auto_now=True)
    achievement_year = models.ForeignKey(AchievementYear,verbose_name="成就年分类")
    achievement_title = models.CharField('标题', max_length=50)
    achievement_text = models.CharField('正文内容', max_length=200)
    achievement_reach = models.IntegerField(verbose_name='是否达成0/1')

    def __unicode__(self):
        return self.achievement_title

    class Meta:
        verbose_name = '成就'
        verbose_name_plural = '成就'