# -*- coding: utf-8 -*-

import scrapy
import re
from scrapy.loader import ItemLoader
from t66ySpider.items import T66YspiderDongmanItem
from t66ySpider.spiders.t66yBaseSpider import t66yBaseSpider

class t66yDongmanSpider(t66yBaseSpider):
    name = 'DongMan'
    start_urls = ["https://www.t66y.com/thread0806.php?fid=5"]
    imgchili_net = re.compile(r'''imgchili''')
    imagetwist_com = re.compile(r'''imagetwist''')
    # croea_com = re.compile(r'''croea.com''')

    def parse_thread(self, response):
        item = T66YspiderDongmanItem()
        item['t_title']         = response.selector.xpath('string(//title)')[0].extract()
        item['t_url']           = response.url

        t_img_l = []
        for link in response.selector.xpath('//input/@src').extract() + response.selector.xpath('//img/@src').extract():
            if self.imgchili_net.search(link):
                t_img_l.append(link.replace('http://t','http://i'))
            elif self.imagetwist_com.search(link):
                t_img_l.append(link.replace('/th/','/i/'))
            # elif self.croea_com.search(link):
            #     t_img_l.append(link.replace('/th','/i/').replace('croea','imagetwist'))
            else:
                t_img_l.append(link)

        item['t_image_list']    = t_img_l
        item['t_torrent_list']  = response.selector.xpath('//a[contains(text(),"rmdown")]/text()').extract()
        yield item
