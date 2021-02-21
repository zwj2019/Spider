# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import json
import traceback
import logging

import EBCodeSearch.settings as settings

logger = logging.getLogger("spiderLogger")
result_data = {}


class EbcodesearchPipeline:
    # 开始爬取时打开文件
    def open_spider(self, spider):
        js_file = os.path.join(settings.OUTPUT_DIR, "%s.json" % spider.name)
        logger.info("Open File : " + js_file)
        try:
            self.file = open(js_file, 'w', encoding='utf-8')
        except:
            logger.error(traceback.format_exc())

    # 爬取结束后关闭文件
    def close_spider(self, spider):
        logger.info("Spider [%s] closed, file closed" % spider.name)
        count = 0
        if spider.name in result_data.keys() :
            result_key_words = result_data[spider.name].keys()
            for key_word in settings.KEY_WORDS_DETAIL.keys():
                if key_word not in result_key_words:
                    continue

                self.file.write(key_word + "\n")
                self.file.write(settings.KEY_WORDS_DETAIL[key_word] + "\n")
                data = result_data[spider.name][key_word]
                count += len(data)
                for d in data:
                    self.file.write(d + "\n")
                self.file.write("\n")
        if spider.name == 'gitee_spider':
            settings.GITEE_COUNT += count
        elif spider.name == 'github_spider':
            settings.GITHUB_COUNT += count
        else:
            settings.GITLAB_COUNT += count
        self.file.flush()
        self.file.close()

    # 处理数据、保存
    def process_item(self, item, spider):
        logger.info("Dump data from spider [%s]" % spider.name)

        key_word, = item
        item = item[key_word]

        try:
            data = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False)
            if spider.name not in result_data.keys():
                result_data[spider.name] = {}
            if key_word in result_data[spider.name].keys():
                result_data[spider.name][key_word].append(data)
            else:
                tmp = [data]
                result_data[spider.name][key_word] = tmp
            # self.file.write(data)
            #             #
            #             # self.file.flush()
        except:
            logger.error(traceback.format_exc())

        return item
