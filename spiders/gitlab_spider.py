import logging
import json
import traceback
import scrapy
from urllib.parse import quote
from EBCodeSearch.items import GitlabItem
import EBCodeSearch.settings as settings
from EBCodeSearch.utils import prepare_key_words
from EBCodeSearch.settings import GITLAB_PRIVATE_TOKEN

logger = logging.getLogger('spiderLogger')
URL2KeyWord = {}


class GitlabSpider(scrapy.Spider):
    name = 'gitlab_spider'

    def start_requests(self):
        key_words_list = settings.KEY_WORDS_DETAIL.keys()

        raw_url = 'https://gitlab.com/api/v4/search?search={}&scope=projects&private_token={}'
        urls = []

        for key_word in key_words_list:
            url = raw_url.format(quote(key_word), GITLAB_PRIVATE_TOKEN)
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
        item = GitlabItem()
        try:
            resp_data = json.loads(response.text)

            if "message" in resp_data and "Unauthorized" in resp_data["message"]:
                logger.error("Private Token may be Expired!")
                return
            url = response.url
            key_word = URL2KeyWord[url]
            settings.VALID_WORDS.add(key_word)

            for content in resp_data:
                namespace = content['namespace']

                item['name'] = namespace['name']                 # 用户名
                item['user_url'] = namespace['web_url']          # 用户主页
                item['repo_url'] = content['web_url']            # 仓库主页
                desc = content['description']                    # 仓库描述
                item['description'] = desc if desc is None or len(desc) < 100 else desc[:100]
                item['created_at'] = content['created_at']       # 仓库创建时间
                item['updated_at'] = content['last_activity_at'] # 仓库更新时间

                yield {key_word : item}

        except Exception as e:
            logger.error(traceback.format_exc())
