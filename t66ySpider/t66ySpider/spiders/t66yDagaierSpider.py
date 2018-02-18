# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from t66ySpider.items import T66YspiderDagaierItem
from t66ySpider.spiders.t66yBaseSpider import t66yBaseSpider


class t66yDagaierSpider(t66yBaseSpider):
    name = 'DaGaiEr'
    start_urls = ["https://www.t66y.com/thread0806.php?fid=16"]

    def parse_thread(self, response):
        l = ItemLoader(item=T66YspiderDagaierItem(), response=response)
        l.add_xpath('t_title', 'string(//title)')
        l.add_xpath('image_urls', '//input/@src')
        return l.load_item()
