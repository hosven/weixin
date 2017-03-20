#coding=utf-8
__author__ = 'wanglu'

import argparse

from wl_flask.main.common.tools import init
from main.config.app_settings import APP_KEY

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--init_db",type=bool,default=False)
    parser.add_argument("--init_path",type=bool,default=True)

    args = parser.parse_args()

    init(args,app_key=APP_KEY)

    from main.main import app

    app.run(host="0.0.0.0",port=8000)

