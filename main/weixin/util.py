#coding=utf-8
__author__ = 'wanglu'

import shelve
import time
import json

import requests

import main.config.app_settings as conf

def get_access_token():
    s = shelve.open("data.dat")
    if s.has_key("access_token"):
        access_token_d = s["access_token"]
        get_time = access_token_d["get_time"]
        access_token = access_token_d["access_token"]
        expires_in = access_token_d["expires_in"]
        if time.time() < get_time+expires_in:
            return access_token

    get_time = time.time()
    APPID = conf.APPID
    APPSECRET = conf.APPSECRET
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (APPID, APPSECRET)
    resp = requests.get(url)
    data = json.loads(resp.content)

    access_token = data["access_token"]

    data["get_time"] = get_time

    s["access_token"] = data

    s.close()

    return access_token

def get_weixin_ip(access_token):
    url = "https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s" % access_token

    resp = requests.get(url)
    return resp.content



if __name__ == "__main__":
    access_token = get_access_token()
    print (get_weixin_ip(access_token))






