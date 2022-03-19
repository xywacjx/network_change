# -*- coding: utf-8 -*-
# 修改ip


#  netsh interface ip set address "VMware Network Adapter VMnet1"  static 192.168.186.2 255.255.255.0 192.168.186.1   修改ip命令，需管理员权限


import os
from this import d
from unicodedata import name

# c=os.popen('ipconfig/all')
# print(c.read())

# macname="VMware Network Adapter VMnet1"
# newip = "192.168.186.3"
# newmask = "255.255.255.0"
# newgetway = "192.168.186.1"

# 拼接命令
# new_change='netsh interface ip set address'+' '+'"%s"'%macname +' '+'static'+' ' + newip+' ' + ' '+ newmask +' '+ newgetway
# print(new_change)
def ip_change(macname,newip,newmask,newgetway):
    new_change='netsh interface ip set address'+' '+'"%s"'%macname +' '+'static'+' ' + newip+' ' + ' '+ newmask +' '+ newgetway
    d=os.system(new_change)
    # 成功返回0 失败1
    # print(d)
    return d
  
        



# ip_change(macname,newip,newmask,newgetway)



