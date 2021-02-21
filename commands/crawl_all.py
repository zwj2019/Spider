import logging

from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError
from scrapy.utils.conf import arglist_to_dict
from EBCodeSearch.utils import send_email, load_key_words
import EBCodeSearch.settings as settings

logger = logging.getLogger("spiderLogger")


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        try:
            opts.spargs = arglist_to_dict(opts.spargs)
        except ValueError:
            raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)

    def run(self, args, opts):
        # read_file()
        load_key_words()
        print(str(settings.KEY_WORDS_DETAIL))
        spider_loader = self.crawler_process.spider_loader

        # 获取EBCodeSearch/spiders下所有的Spider并启动
        for spider_name in args or spider_loader.list():
            logger.info("Spider [%s] start" % spider_name)
            self.crawler_process.crawl(spider_name, **opts.spargs)

        self.crawler_process.start()

        logger.info("Prepare to send email")

        with open('config.txt', 'w', encoding='utf-8') as f:
            for key_word in settings.KEY_WORDS_DETAIL:
                if key_word in settings.VALID_WORDS:
                    f.write(key_word + " : " + settings.KEY_WORDS_DETAIL[key_word] + "\n")

        send_email()
