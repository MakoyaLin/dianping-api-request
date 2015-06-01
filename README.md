Dianping Python Api Demo
========================

## Supported Api
* `get_cities`, [获取支持商户搜索的最新城市列表](http://developer.dianping.com/app/api/v1/metadata/get_cities_with_businesses)
* `get_regions`, [获取支持商户搜索的最新城市下属区域列表](http://developer.dianping.com/app/api/v1/metadata/get_regions_with_businesses)
* `get_categories`, [获取支持商户搜索的最新分类列表](http://developer.dianping.com/app/api/v1/metadata/get_categories_with_businesses)
* `find_businesses`, [搜索商户](http://developer.dianping.com/app/api/v1/business/find_businesses)
* `get_batch_businesses_by_id`, [批量获取指定商户信息](http://developer.dianping.com/app/api/v1/business/get_batch_businesses_by_id)
* `get_recent_reviews`, [获取指定商户最新点评片断](http://developer.dianping.com/app/api/v1/review/get_recent_reviews)
* `get_cities_with_businesses`, [获取支持商户搜索的最新城市列表](http://developer.dianping.com/app/api/v1/metadata/get_cities_with_businesses)

## Example
```python
>>> from dianping import DianpingApi
>>> api = DianpingApi('app_key', 'app_secret')
>>> cities = api.get_cities()
>>> print len(cities)
2628
>>> for city in cities[:3]:
        print city,

全国 上海 北京
>>> regions = api.get_regions(city=u'全国')
Traceback (most recent call last):
  File "dianping.py", line 80, in <module>
    regions = api.get_regions(cities[0])
  File "dianping.py", line 63, in get_regions
    result = self.request('metadata/get_regions_with_businesses', data)
  File "dianping.py", line 52, in request
    '%s - %s' % (error['errorCode'], error['errorMessage']))
__main__.DianpingApiError: 10011 - Parameter value is invalid: city. (请求参数值无效: city)
>>> regions = api.get_regions(city=u'北京')
>>> print regions[0]['city_name']
北京
>>> for region in regions[0]['districts'][0]['neighborhoods'][:3]:
        print region,

朝阳其它 安贞 劲松/潘家园
>>>
```
