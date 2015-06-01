#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append("..")

from db import _db as db
from dianping import DianpingApi


if __name__ == '__main__':

    api = DianpingApi('85719554', 'b9aafd8a60e1435faf7ba3389cdb4e9a')
    cities = api.get_cities_with_businesses()
    db.cities.remove()
    db.cities.save({'cities': cities})
