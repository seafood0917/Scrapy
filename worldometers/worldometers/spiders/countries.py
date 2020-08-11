# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        #title = response.xpath("//h1/text()").get()
        #countries = response.xpath("//td/a/text()").getall()
        #populations = response.xpath("//tr/td/text()").getall()
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            #absolute_link = f"https://www.worldometers.info{link}"
            #absolute_link = response.urljoin(link)
            #yield scrapy.Request(url=absolute_link)

            yield response.follow(url=link)
