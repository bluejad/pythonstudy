# # # #-*- coding:utf-8 -*-
# # # '''
# # # 简短地生成随机密码，包括大小写字母、数字，可以指定密码长度
# # # '''
# # # #生成随机密码
# # # from random import choice
# # # import string
# # #
# # # #python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
# # #
# # # def GenPassword(length=8,chars=string.ascii_letters+string.digits):
# # #     return ''.join([choice(chars) for i in range(length)])
# # #
# # # pawdtemp = GenPassword(8)
# # #
# # # print pawdtemp
# # # print "3333333333333333"
# # # print pawdtemp
# # #
# # # emailaddress = '3357008695@qq.com'
# # #
# # # from django.core.mail import send_mail
# # # send_mail('Subject', 'pawdtemp', 'python_smtp_test@163.com', [emailaddress], fail_silently=False)
# # #
# # # #密码表
# # # password_list = [789,123456]
# # # #正确密码
# # # password_correct = 123456
# # # #修改密码暗号
# # # password_change = 789
# # #
# # # #声明变量count为0
# # # count = 0
# # #
# # # def account_login():
# # #     #接受终端输入的密码
# # #     password = input('Password:')
# # #     #声明他们量都是全局变量
# # #     global password_list
# # #     global count
# # #     #开始循环
# # #     while count<3:
# # #         #当密码正确的时候,直接退出
# # #         if password == password_list[-1]:
# # #             print('Login Success!congratulations!')
# # #             exit()
# # #         #当密码为修改密码的暗号的时候,把新输入的密码追加到密码表中,再尝试重新登录
# # #         elif password == password_list[0]:
# # #             new_password = input('Enter a new password:')
# # #             password_list.append(new_password)
# # #             print('Change password Success!congratulations!')
# # #             account_login()
# # #         else:
# # #             #当密码错误的时候,全局变量计数增加,如果输错3次就不符合循环条件了
# # #             count = count + 1
# # #             print('Wrong password or invalid input',count)
# # #             account_login()
# # #     else:
# # #         print('Your account has been suspended')
# # #
# # # #直接调用上面定义的这个函数
# # # account_login()
# # #
# # # import json
# # # print('{0} a word she can get what she {1} for'.format('With','came'))
# # #
# # # from functools import reduce
# # #
# # # class convertstrtoint:
# # #     _name = "zhangkun333"
# # #     __namedede = "zhangkun444"
# # #
# # #     def get_namedede(self):
# # #         return self.__namedede
# # #
# # #     def set_namedede(self,s):
# # #         self.__namedede = s
# # #
# # # print convertstrtoint._name
# # # rrr = convertstrtoint()
# # # print rrr.get_namedede()
# # # you = "you"
# # # rrr.set_namedede(you)
# # # print rrr.get_namedede()
# # # print rrr._convertstrtoint__namedede
# # #
# # #
# # # from multiprocessing import Process
# # # import os
# # #
# # # def run_proc(name):
# # #     print ("child process %s (%s)" % (name,os.getpid()))
# # #
# # # if __name__=='__main__':
# # #     print "parents process %s" % os.getpid()
# # #     p = Process(target=run_proc,args=('test',))
# # #     print 'child is starting'
# # #     p.start()
# # #     p.join()
# # #     print "child process end"
# #
# #
# # # from multiprocessing import Pool
# # # import os,time,random
# # #
# # # def long_time_task(name):
# # #     print "run_tasl %s %s" % (name,os.getpid())
# # #     start = time.time()
# # #     time.sleep(random.random()*3)
# # #     end = time.time()
# # #     print "task %s runs %0.2f seconds" % (name,(end-start))
# # #
# # # if __name__ == '__main__':
# # #     print "parents %s"% os.getpid()
# # #     p = Pool(4)
# # #     for i in range(5):
# # #         p.apply_async(long_time_task,args=(i,))
# # #     print "waiting for all subprocess done..."
# # #     p.close()
# # #     p.join()
# # #     print "all subprocess done"
# # #
# # # import subprocess
# # #
# # # print "$ nslookup www.python.org"
# # # r = subprocess.call(['nslookup','www.python.org'])
# # # print 'Exit code:',r
# # def consumer():
# #     r=str
# #     while 1:
# #         n = yield r
# #         print ('first mome')
# #         if not n:
# #             return
# #         print ('[CONSUMER] Consuming %s...' % n)
# #         r='200 ok'
# #
# # def produce(c):
# #     c.send(None)
# #     n=0
# #     while n<5:
# #         n+=1
# #         print('[PRODUCER] Producing %s...' % n)
# #         r = c.send(n)
# #         print('[PRODUCER] Consumer return:%s' %r)
# #     c.close()
# #
# # c = consumer()
# # produce(c)
# # def f():
# #     print 'a'
# #     yield 1
# #     print 'b'
# #     yield 2
# #     print 'c'
# #
# # g = f()
# # print 'start'
# # print g.next()
# # print 'next'
# # print g.next()
# # my_generator = (x*x for x in range(4))
# # print dir(my_generator)
# #
# # for i in my_generator:
# #     print i
# #
# #
# # for i in my_generator:
# #     print i
# #
# # def g():
# # # 	yield 0
# # # 	yield 1
# # # 	yield 2
# # #
# # # lalalal = g()
# # # print type(lalalal)
# # # print lalalal.next(),lalalal.next(),lalalal.next(),lalalal.next(),lalalal.next(),lalalal.next(),lalalal.next()
# # # print lalalal.next()
# # # print lalalal.next()
# # # print lalalal.next()
# # # print lalalal.next()
# # # print lalalal.next()
# # # print lalalal.next()
# # #
# #
# # def r_return(n):
# #      print "You taked me."
# #      while n > 0:
# #          print "before return"
# #
# #          return n
# #          n -= 1
# #          print "after return"
# # rr = r_return(3)
# # print rr
# #
# #
# # def r_return(n):
# #     print "You taked me."
# #     while n > 0:
# #         print "before return"
# #
# #         yield n
# #         n -= 1
# #         print "after return"
# #
# #
# # rr = r_return(3)
# # print rr.next()
# # print rr.next()
# # print rr.next()
#
# # def repeater():
# #     n=None
# #     while 1:
# #         print "1"
# #         n=(yield n)
# #         print len(n)
# #         print "2222222222222222"
# #
# #
# # r= repeater()
# # r.next()
# # print r.send("new friend come in")
# # print r.send("tseeee")
#
# # import select
# # import socket
# # import sys
# #
# # HOST = 'localhost'
# # PORT = 5000
# # BUFFER_SIZE = 1024
# #
# # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # server.bind(HOST,PORT)
# # server.listen(5)
# #
# # inputs = [server, sys.stdin]
# # running = True
#
# # import platform
# # #获取操作系统名称及版本号
# # print platform.platform()
# #
# # import os
# # cwd = os.getcwd()
# # # 获取当前目录路径
# # file_list = os.listdir(cwd)
# # #过滤掉隐藏文件
# # r = [i for i in file_list if not i.startswith('.')]
# # # 排序及打印
# # r.sort()
# # for i in r:
# #     print i
#
# # import random
# # ponit = random.randrange(1,7)
# # print ponit
# # alalal = []
# # alalal.append(ponit)  #append()函数是在列表末尾添加新的对象
# # print dir(str)
# # def sum(item,a=[]):
# #     a.append(item)
# #     return a
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #5
#
#
# # L=list(input())
# # array=L[1]
# # target=L[0]
# # print array
# # print target
# #
# # def Find(target, array):
# #     n = len(array)
# #     print n
# #     flag = 'false'
# #     for i in range(n):
# #         print array[i]
# #         if target in array[i]:
# #             flag = 'true';
# #             print flag
# #             print array[i]
# #             print flag
# #
# # print Find(target,array)
#
# # -*- coding:utf-8 -*-
# # class Solution:
# #     # array 二维列表
# #     def Find(self, target, array):
# #         # write code here
# #         n = len(array)
# #         for i in xrange(n):
# #             print array[i]
# #             if target in array[i]:
# #                 return "find it"
# #             else:
# #                 continue
# #
# # s = Solution()
# # array = input()
# # target = input()
# # print s.Find(target, array)
#
# tempTuple = (1,2,3,4)
# print range(3,-1,-1)
# print range(-1,3,1)
# #
# # for i in range(len(tempTuple)-1,-1,-1):
# #     print i
#     # print tempTuple[i]
# tempstr = "hello you hello python are you ok Use python is good"
# print tempstr.replace("you","python")
#
# import re
# rex = r'(hello|Use)'
# print re.sub(rex,"Bye",tempstr)
#
# def SingleTon(cls,*args,**kwargs):
#     instances = {}
#     print instances
#     def _singleton():
#         if cls not in instances:
#             instances[cls] = cls(*args,**kwargs)
#         print instances
#         return instances[cls]
#     return _singleton
#
# @SingleTon
# class LastClass(object):
#     a = 1
# test1 = LastClass()
# print test1.a
# test2 = LastClass()
# print test2.a


# class SignalTon(type):
#     def __init__(cls,name,bases,dict):
#         super(SignalTon, cls).__init__(name,bases,dict)
#         cls._instance = None
#
#     def __call__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(SignalTon,cls).__call__(*args,**kwargs)
#         return cls._instance
#
# class TestClass(object):
#     __metaclass__ = SignalTon
#
# test1 = TestClass()
# test2 = TestClass()
#
# test1.a = 2
# print test1.a,test2.a
# print id(test1),id(test2)

# class SingleTon(object):
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         obj = object.__new__(cls,*args,**kwargs)
#         obj.__dict__ = cls._state
#         return obj
#
# class TestClass(SingleTon):
#     a = 1
#
# test1 = TestClass()
# test2 = TestClass()
# print test1.a,test2.a
# test1.a = 2
# print test1.a,test2.a
# print id(test1),id(test2)
# str = "  qq  ee  rr  "
# print str.strip()
# def rightStrip(tempStr,splitStr):
#     endindex = tempStr.rfind(splitStr)
#     while endindex != -1 and endindex == len(tempStr) - 1:
#          tempStr = tempStr[:endindex]
#          endindex = tempStr.rfind(splitStr)
#     return tempStr
#
# def leftStrip(tempStr,splitStr):
#     startindex = tempStr.find(splitStr)
#     while startindex == 0:
#         tempStr = tempStr[startindex+1:]
#         startindex = tempStr.find(splitStr)
#     return tempStr
#
# str = "  H  "
# print str
# print leftStrip(str,' ')
# print rightStrip(str,' ')
def print_msg():
    # print_msg 是外围函数
    msg = "zen of python"
    def printer():
        # printer 是嵌套函数
        print(msg)
    return printer

another = print_msg()
print 888888888888
# 输出 zen of python
another()