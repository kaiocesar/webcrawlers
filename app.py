__author__ = 'Admin'
# -*- coding: utf-8 -*-

import scrapy


class BlackFridaySpider(scrapy.Spider):
    name = 'BlackFriday'
    allowed_domains = ['extra.com.br']
    start_url = ('http://www.extra.com.br/TelefoneseCelulares/celular/?Filtro=C38_C39&nid=200526')


    def parse(self, response):
        self.log('Hello world {0}'. format(response.url))