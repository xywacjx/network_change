# -*- coding:utf-8 -*-
# 获取网关信息

import psutil
import os



d=os.popen("ipconfig/all").readlines()


print(d)




