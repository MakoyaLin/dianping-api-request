#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append("..")

from db import _db as db
from dianping import DianpingApi


if __name__ == '__main__':

    api = DianpingApi('85719554', 'b9aafd8a60e1435faf7ba3389cdb4e9a')
    city = u'上海'
    regions = api.get_regions(city)
    #db.regions.insert(regions)

    categories = (u'宠物', u'宠物店', u'宠物医院')
    neighborhoods = []
    for district in regions[0]['districts']:
        neighborhoods += district['neighborhoods']
    businesses = []
    param = {}
    param['city'] = city
    for neighborhood in neighborhoods:
        param['region'] = neighborhood
        for category in categories:
            param['category'] = category
            businesses += api.find_businesses(**param)
        break
    #db.business.insert(businesses)
    for business in businesses:
        db.business.update({'business_id': business['business_id']}, {'$set': business}, upsert=True)
