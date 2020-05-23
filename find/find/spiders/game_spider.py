# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from find.items import GameItem

class GameSpiderSpider(CrawlSpider):
    name = 'game_spider'
    allowed_domains = ['8i99.com']
    start_urls = 'https://www.8i99.com/forum.php?mod=forumdisplay&fid=2&sortid=1&sortid=1&page=1'
    login_url = 'https://www.8i99.com/member.php?mod=logging&action=login'
    login_form_url = 'https://www.8i99.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LGNee&inajax=1'


    rules = (
        # Rule(LinkExtractor(allow=r'.+mod=forumdisplay&fid=2&sortid=1&sortid=1&page=\d+'),
        #      follow=True),
        Rule(LinkExtractor(restrict_xpaths=u"//a[text()='下一页']"),
             follow=True,callback='parse_item'),
    )

    def start_requests(self):
        yield scrapy.Request(url=self.login_url, callback=self.post_login)

    def post_login(self, response):
        data = {'username': 'njchangwei',
                'password': '19800121',
                }
        yield scrapy.FormRequest(url=self.login_form_url, formdata=data, callback=self.after_login)

    def after_login(self, response):
        yield scrapy.Request(url=self.start_urls, callback=self.parse)


    def parse_item(self, response):
        divs = response.xpath("//form[@id='moderate']/li")
        for div in divs:
            item = GameItem()
            item['title'] = div.xpath(".//div[@class='nex_sologame_list_title']/a/b//text()").get(0)
            item['language'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[1]/text()").extract()[0]
            item['type'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[2]/text()").extract()[0]
            item['form'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[3]/i//text()").get(0)
            item['sellingtime'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[4]/text()").extract()[0]
            item['updatetime'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[5]/text()").extract()[0]
            yield item


    def parse_start_url(self,response):
        divs = response.xpath("//form[@id='moderate']/li")
        for div in divs:
            item = GameItem()
            item['title'] = div.xpath(".//div[@class='nex_sologame_list_title']/a/b//text()").get(0)
            item['language'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[1]/text()").extract()[0]
            item['type'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[2]/text()").extract()[0]
            item['form'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[3]/i//text()").get(0)
            item['sellingtime'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[4]/text()").extract()[0]
            item['updatetime'] = div.xpath(".//div[@class='nex_sologame_intels']/dl/dd[5]/text()").extract()[0]
            yield item


