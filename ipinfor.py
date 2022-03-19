# -*- coding: utf-8 -*-
#! python3
from ipaddress import ip_address
from unicodedata import name
import psutil

# 获取网卡名称ip字典,网卡名字集合

def get_netcard():
    netcard_info = {}
    info = psutil.net_if_addrs()
    # print(info.items())
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1':
                netcard_info[k]=item[1]
    return netcard_info

get_netcard()
# 获得网卡名称集合
def get_mac():
    mac_info=[]
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1':
                mac_info.append(k)
    # print(mac_info)
    return mac_info

# 获得网卡、子网掩码字典
def get_yanmainfo():
    yanma_info = {}
    info = psutil.net_if_addrs()
    # print(info.items())
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1':
                yanma_info[k]=item[2]
    return yanma_info


# 获取指定网卡ip
def get_ip(name):
    dict=get_netcard()
    ip_info=dict[name]
    return ip_info


# 获取指定网卡掩码
def get_yanma(name):
    dict=get_yanmainfo()
    yanmainfo=dict[name]
    return yanmainfo

# 获取指定网卡网关



# print(get_yanma('本地连接'))

# if __name__ == '__main__':
#     print (get_netcard()) 
#     print(get_ip('本地连接'))
