# Create your views here.
# -*- coding: utf-8 -*-

import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import urllib

#django默认开启csrf防护，这里使用@csrf_exempt去掉防护
@csrf_exempt
@csrf_exempt
def weixin_main(request):
    if request.method == "GET":
        #接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        #服务器配置中的token
        token = 'Pythonnav'
        #把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
		  return HttpResponse(echostr)
        else:
          return HttpResponse("field")
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)

#微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法
import xml.etree.ElementTree as ET
def autoreply(request):
    try:
        webData = request.body
        xmlData = ET.fromstring(webData)

        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        MsgType = xmlData.find('MsgType').text
        MsgId = xmlData.find('MsgId').text

        toUser = FromUserName
        fromUser = ToUserName

        if msg_type == 'text':
            content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
            replyMsg = TextMsg(toUser, fromUser, content)
            print "成功了!!!!!!!!!!!!!!!!!!!"
            print replyMsg
            return replyMsg.send()

        elif msg_type == 'image':
            content = "图片已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'voice':
            content = "语音已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'video':
            content = "视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'shortvideo':
            content = "小视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'location':
            content = "位置已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        else:
            msg_type == 'link'
            content = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()

    except Exception, Argment:
        return Argment

class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text

import time
class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)
#
# #接口获取
# class Basic:
#     def __init__(self):
#         self.__accessToken = ''
#         self.__leftTime = 0
#
#     def __real_get_access_token(self):
#         appId = "wx3190516e558663f4"
#         appSecret = "e931907f440a52c45fbff5b179c348fa"
#
#         postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
#                    "client_credential&appid=%s&secret=%s" % (appId, appSecret))
#         urlResp = urllib.urlopen(postUrl)
#         urlResp = json.loads(urlResp.read())
#
#         self.__accessToken = urlResp['access_token']
#         self.__leftTime = urlResp['expires_in']
#
#     def get_access_token(self):
#         if self.__leftTime < 10:
#             self.__real_get_access_token()
#         return self.__accessToken
#
#     def run(self):
#         while (True):
#             if self.__leftTime > 10:
#                 time.sleep(2)
#                 self.__leftTime -= 2
#             else:
#                 self.__real_get_access_token()
#
#
# class Menu(object):
#     def __init__(self):
#         pass
#
#     def create(self, postData, accessToken):
#         postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
#         if isinstance(postData, unicode):
#             postData = postData.encode('utf-8')
#         urlResp = urllib.urlopen(url=postUrl, data=postData)
#         print urlResp.read()
#
#     def query(self, accessToken):
#         postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
#         urlResp = urllib.urlopen(url=postUrl)
#         print urlResp.read()
#
#     def delete(self, accessToken):
#         postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
#         urlResp = urllib.urlopen(url=postUrl)
#         print urlResp.read()
#
#     # 获取自定义菜单配置接口
#     def get_current_selfmenu_info(self, accessToken):
#         postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
#         urlResp = urllib.urlopen(url=postUrl)
#         print urlResp.read()
#
#
# postJson = """
# {
#     "button":
#     [
#         {
#             "type": "click",
#             "name": "开发指引",
#             "key":  "mpGuide"
#         },
#         {
#             "name": "公众平台",
#             "sub_button":
#             [
#                 {
#                     "type": "view",
#                     "name": "更新公告",
#                     "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
#                 },
#                 {
#                     "type": "view",
#                     "name": "接口权限说明",
#                     "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
#                 },
#                 {
#                     "type": "view",
#                     "name": "返回码说明",
#                     "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
#                 }
#             ]
#         },
#         {
#             "type": "media_id",
#             "name": "旅行",
#             "media_id": "z2zOokJvlzCXXNhSjF46gdx6rSghwX2xOD5GUV9nbX4"
#         }
#       ]
# }
# """
# def startmymenu(request):
#     myMenu = Menu()
#     accessToken = Basic().get_access_token()
#     myMenu.create(postJson, accessToken)
#     print accessToken
#     return HttpResponse(postJson)
