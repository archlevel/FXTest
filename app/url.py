# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 20:05:32
# @Author  : lileilei
'''url'''
from app.views import *
from app import app
app.add_url_rule('/load/<string:filename>',view_func=LoadView.as_view('load'))
app.add_url_rule('/getyongli',view_func=Getyongli.as_view('getyongli'))