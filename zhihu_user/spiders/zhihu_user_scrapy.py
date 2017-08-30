# coding=utf-8

import scrapy
from zhihu_user.items import ZhihuUserItem
import json
#sleepsheep-4

class ZhUserSpider(scrapy.Spider):
    name = "zhihuuser"

    allowed_domains = ["www.zhihu.com"]
    user_url = "https://www.zhihu.com/api/v4/members/{user}?include={include}"
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&amp;offset={offset}&amp;limit={limit}'
    start_user = 'excited-vczh'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        yield scrapy.Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        yield scrapy.Request(
            self.follows_url.format(user=self.start_user, include=self.follows_query, limit=20, offset=0),
            self.parse_follows)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = ZhihuUserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield scrapy.Request(
            self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0),
            self.parse_follows)

    def parse_follows(self, response):
        results = json.loads(response.text)
        if 'data' in results:
            for result in results.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                                     self.parse_user)

        if 'paging' in results and results.get('paging').get('is_end') == False:
            next_page_url = results.get('paging').get('next')
            yield scrapy.Request(
                next_page_url,
                self.parse_follows)
