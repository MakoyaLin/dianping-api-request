#!/usr/bin/env python
# coding=utf-8

import hashlib
import urllib

APPKEY = ""
SECRET = ""

def api_request(apiUrl, paramSet):
    #参数排序与拼接
    paramMap = {}
    for pair in paramSet:
        paramMap[pair[0]] = pair[1]

    codec = APPKEY
    for key in sorted(paramMap.iterkeys()):
        codec += key + paramMap[key]

    codec += SECRET

    #签名计算
    sign = (hashlib.sha1(codec).hexdigest()).upper()

    #拼接访问的URL
    url_trail = "appkey=" + APPKEY + "&sign=" + sign
    for pair in paramSet:
        url_trail += "&" + pair[0] + "=" + pair[1]

    requestUrl = apiUrl + "?" + url_trail

    #模拟请求
    response = urllib.urlopen(requestUrl)

    return response.read()

if __name__ == '__main__':
    # get_batch_businesses_by_id
    # http://developer.dianping.com/app/api/v1/business/get_batch_businesses_by_id
    apiUrl = "http://api.dianping.com/v1/business/get_batch_businesses_by_id"
    paramSet = []
    paramSet.append(("format", "json"))
    paramSet.append(("business_ids", "6110204"))

    # find_businesses
    # http://developer.dianping.com/app/api/v1/business/find_businesses
    #apiUrl = "http://api.dianping.com/v1/business/find_businesses"
    #paramSet = []
    #paramSet.append(("city", "上海"))

    print api_request(apiUrl, paramSet)
