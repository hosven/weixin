#coding=utf-8
__author__ = 'wanglu'

import os

from wl_flask.main.main import *
from wl_flask.main.common.util import get_app_path
from .rest_api.weixin_api import weixin_blueprint
from .config.app_settings import APP_KEY

app.register_blueprint(weixin_blueprint, url_prefix='/'+rest_api_no_db)

@app.route("/static/<path>")
def weixin(path):
    app_path = get_app_path(APP_KEY)
    static = os.path.join(app_path,"main/static")
    return send_from_directory(static,path)

