import logging
import json
import traceback
import scrapy
from urllib.parse import quote
import EBCodeSearch.settings as settings
from EBCodeSearch.items import GiteeItem
# from EBCodeSearch.utils import prepare_key_words

logger = logging.getLogger('spiderLogger')
URL2KeyWord = {}


class GiteeSpider(scrapy.Spider):
    name = 'gitee_spider'

    def start_requests(self):
        key_words_list = settings.KEY_WORDS_DETAIL.keys()

        raw_url = 'https://gitee.com/api/v5/search/repositories?q={}'
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
            logger.warning("response status of %s is %d" % (response.url, response.status))
            return

        item = GiteeItem()
        try:
            resp_data = json.loads(response.text)
            url = response.url
            key_word = URL2KeyWord[url]
            settings.VALID_WORDS.add(key_word)

            for content in resp_data:
                owner = content['owner']

                item['name'] = owner['name']
                item['private'] = content['private']          # 仓库是否私有
                item['user_url'] = owner['html_url'][:-4]     # 用户主页
                item['repo_url'] = content['html_url']        # 仓库主页
                desc = content['description']                 # 仓库描述
                item['description'] = desc if desc is None or len(desc) < 100 else desc[:100]
                item['created_at'] = content['created_at']    # 仓库创建时间
                item['updated_at'] = content['updated_at']    # 仓库更新时间

                yield {key_word : item}
        except Exception as e:
            logger.error(traceback.format_exc())
