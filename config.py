# -*- coding: UTF-8 -*-
import os

BASE_DIR = os.path.dirname(__file__)

# 参数
options = {
    "port": 9000
}

# 配置
settings = {
    "debug": True,
    "static_path": os.path.join(BASE_DIR, "static"),
    "template_path": os.path.join(BASE_DIR, "templetes"),
}
