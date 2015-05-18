#!/usr/bin/env python
# coding=utf-8

import json

from db import _db as db
from api_request import api_request


if __name__ == '__main__':
    # http://developer.dianping.com/app/api/v1/business/get_batch_businesses_by_id
    apiUrl = "http://api.dianping.com/v1/business/get_batch_businesses_by_id"
    paramSet = []
    paramSet.append(("format", "json"))
    paramSet.append(("business_ids", "6110204,6110205"))

    data = api_request(apiUrl, paramSet)
    data = json.loads(data, encoding='utf-8')
    status = data['status']
    businesses = data['businesses']

    if status == 'OK':
        #db.business.insert(businesses)
        for business in businesses:
            #db.business.update({'business_id': business['business_id']}, {'$set': business}, upsert=True)
            db.business.save({'_id': business['business_id'], 'data': business})
