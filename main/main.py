#coding=utf-8
__author__ = 'wanglu'

import logging
import logging.config

from flask import Flask,request

from .config import app_settings as conf

logging.config.dictConfig(conf.LOGGING_CONFIG)

app = Flask(__name__)

# Flask app configuration
app.config.from_object("main.config.app_settings")  # default config settings

from .rest_api.test_api import test_blueprint
from .rest_api.weixin_api import weixin_blueprint

rest_api_name = 'api'
app.register_blueprint(test_blueprint, url_prefix='/'+rest_api_name)
app.register_blueprint(weixin_blueprint)



