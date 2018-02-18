# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from t66ySpider.items import T66YBaseItem


class t66yBaseSpider(scrapy.Spider):
    allowed_domains = ['www.t66y.com']
    unicode_next_page = u'\u4e0b\u4e00\u9801'

    def parse(self, response):
        thread_hrefs = response.xpath('//h3/a/@href')

        for thread_href in thread_hrefs:
            thread_url = response.urljoin(thread_href.extract())
            yield scrapy.Request(thread_url, callback=self.parse_thread)

        next_page_href = response.xpath(
            "//a[text()='%s']/@href" % self.unicode_next_page)[0]
        next_page_url = response.urljoin(next_page_href.extract())

        #yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_thread(self, response):
        l = ItemLoader(item=T66YBaseItem(), response=response)
        l.add_xpath('t_title', 'string(//title)')
        l.add_xpath('image_urls', '//input/@src')
        return l.load_item()
