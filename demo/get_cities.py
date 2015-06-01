#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append("..")

from db import _db as db
from dianping import DianpingApi

api = DianpingApi('85719554', 'b9aafd8a60e1435faf7ba3389cdb4e9a')


def get_regions(city):
    districts = api.get_regions(city=city)[0]['districts']
    regions = []
    for district in districts:
        regions.extend(district['neighborhoods'])
    return regions


def get_cities():
    cities = api.get_cities()
    city_list = [{'city_name': city} for city in cities]
    return city_list


def update_regions(city, regions):
    db.cities.update({'city_name': city}, {'$set': {'regions': regions}})


def save_cities(cities):
    db.cities.remove()
    db.cities.insert(cities)


if __name__ == '__main__':
    cities = get_cities()
    save_cities(cities)

    cities = db.cities.find()
    for city in cities:
        city = city['city_name']
        print city
        if city == u'全国':
            continue
        regions = get_regions(city)
        update_regions(city, regions)
        break
