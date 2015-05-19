#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append("..")

from db import _db as db
from dianping import DianpingApi


if __name__ == '__main__':

    api = DianpingApi('85719554', 'b9aafd8a60e1435faf7ba3389cdb4e9a')
    businesses = db.business.find()
    for business in businesses:
        business_id = business['business_id']
        reviews = api.get_recent_reviews(business_id)
        db.business.update({'business_id': business_id}, {'$set': {'reviews': reviews}})
