# -*- coding: utf-8 -*-
from scrapy import signals

class ProxyDownloaderMiddleware(object):
    @classmethod
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://127.0.0.1:1080"
        return None