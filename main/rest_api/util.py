#coding=utf-8
__author__ = 'wanglu'

from flask import jsonify

def render_json(response_data=None,**kwargs):
    response = {}

    if response_data:
        response = response_data

    return jsonify(content=response,**kwargs)

