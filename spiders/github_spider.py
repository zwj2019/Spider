import logging
import json
import traceback
from urllib.parse import quote
import scrapy

from EBCodeSearch.items import GithubItem
from EBCodeSearch.utils import prepare_key_words
import EBCodeSearch.settings as settings

logger = logging.getLogger('spiderLogger')
URL2KeyWord = {}


class GithubSpider(scrapy.Spider):
    name = 'github_spider'

    def start_requests(self):
        key_words_list = settings.KEY_WORDS_DETAIL.keys()

        raw_url = 'https://api.github.com/search/repositories?q={}&per_page=30'
        urls = []

        for key_word in key_words_list:
            url = raw_url.format(quote(key_word))
            urls.append(url)
            URL2KeyWord[url] = key_word

        for url in urls:
            logger.info("Request URL : " + url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        if response.status != 200:
            logger.warning("Response status from %s is %d" % (response.url, response.status))
            return

        logger.info("Parsing data from " + response.url)
        item = GithubItem()
        try:
            resp_data = json.loads(response.text)
            url = response.url
            key_word = URL2KeyWord[url]

            settings.VALID_WORDS.add(key_word)

            for content in resp_data['items']:
                owner = content['owner']

                item['name'] = owner['login']                 # 用户名
                item['private'] = content['private']          # 仓库是否私有
                item['user_url'] = owner['html_url']          # 用户主页
                item['repo_url'] = content['html_url']        # 仓库主页
                desc = content['description']                 # 仓库描述
                item['description'] = desc if desc is None or len(desc) < 100 else desc[:100]
                item['created_at'] = content['created_at']    # 仓库创建时间
                item['updated_at'] = content['updated_at']    # 仓库更新时间

                yield {key_word : item}
        except Exception as e:
            logger.error(traceback.format_exc())

