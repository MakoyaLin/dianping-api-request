#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient

_connection = MongoClient('localhost')
_db = _connection['dianping']
