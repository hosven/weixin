#coding=utf-8
__author__ = 'wanglu'

import hashlib

from flask import Blueprint,request

from ..weixin import receive
from ..weixin import reply
import main.config.app_settings as conf

weixin_blueprint = Blueprint("weixin_blueprint",__name__)

@weixin_blueprint.route("/",methods=["GET","POST"])
def index():

    try:
        if request.method == "GET":
            signature = request.args["signature"]
            echostr = request.args["echostr"]
            timestamp = request.args["timestamp"]
            nonce = request.args["nonce"]

            token = conf.APP_TOKEN

            list = [token,timestamp,nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature

            if hashcode == signature:
                return echostr
            else:
                return ""

        if request.method == "POST":
            webData = request.data
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if  recMsg.MsgType == 'text':
                    if recMsg.Content == "test":
                        content = "test"
                    elif recMsg.Content == "baidu":
                        content = "test http://www.baidu.com"
                    else:
                        content = "test"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            elif isinstance(recMsg,receive.Event):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.Event == "VIEW":
                    content = "Menu Event View"
                    replyMsg = reply.TextMsg(toUser,fromUser,content)
                    return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
    except Exception,err:
        return "error"





