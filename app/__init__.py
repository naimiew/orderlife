# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)  # 创建应用对象
app.config.from_object('config')

from app import views  # 导入视图模块
