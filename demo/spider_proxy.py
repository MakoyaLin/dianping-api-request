#!/usr/bin/env python
# coding=utf-8

import urllib2

def get_url_data(url, proxy):
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

    i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'}
    req = urllib2.Request(url, headers=i_headers)
    html = urllib2.urlopen(req)
    return html.read()


if __name__ == '__main__':
    url = 'http://v3.bootcss.com/'
    proxy = {'http':'202.106.16.36:3128'}
    data = get_url_data(url, proxy)
    print data
