#coding:utf-8
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import AchievementYear,Achievement
import datetime

# Create your views here.

#所有
def index(request):
    if request.user.is_authenticated():
        # 获取问题所有分类
        a = AchievementYear.objects.all()
        es = []
        for e in a:
            # es.append(Achievement.objects.filter(achievement_year=e.achievement_date))
            #print len(Achievement.objects.filter(achievement_year=e))
            es.append((e.achievement_date,e.achievement_summary,len(Achievement.objects.filter(achievement_year=e))))
        #return HttpResponse(es)
        return render(request,'achievement/index.html',{'es': es})
    else:
        return redirect('pythonnav:SIGN_IN_NOW')

def set_year_summary(request):
    achievement_date = request.POST['year']
    achievement_summary = request.POST['achievement_text']
    twz = AchievementYear.objects.get(achievement_date=achievement_date)
    print twz
    twz.achievement_summary = achievement_summary
    twz.save()
    return redirect('achievement:index')

#今年
def achievement(request):
    if request.user.is_authenticated():
        yearcategory = AchievementYear.objects.get(achievement_date=str(datetime.datetime.now().year))
        a = Achievement.objects.filter(achievement_year = yearcategory)
        es = []
        for e in a:
            es.append((e.id, e.achievement_date, e.achievement_title, e.achievement_reach))

        return render(request,'achievement/basic_table.html', {'es': es})
    else:
        return redirect('pythonnav:SIGN_IN_NOW')


def set_new_purpose(request):
    achievement_title = request.POST['achievement_title']
    achievement_text = request.POST['achievement_text']
    yearcategory = AchievementYear.objects.get(achievement_date = str(datetime.datetime.now().year))
    print type(yearcategory)

    qqqq = Achievement(achievement_title=achievement_title, achievement_text=achievement_text, achievement_author=request.user, achievement_year = yearcategory,achievement_reach=0)
    qqqq.save()
    return redirect('achievement:achievement')

def changestate(request,id):

    twz = Achievement.objects.get(id=id)
    if twz.achievement_reach == 0:
        twz.achievement_reach = 1
        twz.save()
    elif twz.achievement_reach == 1:
        twz.achievement_reach = 0
        twz.save()
    else:
        pass

    return redirect('achievement:achievement')

def viewcontent(request,id):
    achievementcontent = Achievement.objects.filter(id=id)
    #return HttpResponse(achievementcontent)
    return render(request, 'achievement/form_validation.html', {'achievementcontent': achievementcontent})

def deleteone(request,id):
    Achievement.objects.filter(id=id).delete()
    return redirect('achievement:achievement')

def yearcontent(request,year):
    yearcategory = AchievementYear.objects.get(achievement_date=year)
    a = Achievement.objects.filter(achievement_year=yearcategory)
    es = []
    for e in a:
        es.append((e.id, e.achievement_date, e.achievement_title, e.achievement_reach))
    year=year
    return render(request,'achievement/yearcontent.html', {'es': es,'year':year})