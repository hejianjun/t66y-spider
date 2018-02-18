# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.files import FilesPipeline

class T66YspiderPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            print('file_url: %s', file_url)
            yield scrapy.Request(file_url)
    