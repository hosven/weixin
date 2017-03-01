#coding=utf-8
__author__ = 'wanglu'

from flask import Blueprint,request

from util import *

test_blueprint = Blueprint("test_blueprint",__name__)

@test_blueprint.route("/test/add_test/<name>",methods=["GET"])
def add_order(name):

    return render_json()

@test_blueprint.route("/test/add_user/<username>/<password>",methods=["GET"])
def add_user(username,password):

    return render_json()


