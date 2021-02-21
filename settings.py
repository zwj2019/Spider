# Scrapy settings for EBCodeSearch project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
import collections

BOT_NAME = 'EBCodeSearch'

SPIDER_MODULES = ['EBCodeSearch.spiders']
NEWSPIDER_MODULE = 'EBCodeSearch.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'EBCodeSearch.middlewares.EbcodesearchSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'EBCodeSearch.middlewares.EbcodesearchDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'EBCodeSearch.pipelines.EbcodesearchPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


##################
# Data Configure #
##################
# 数据存放目录
OUTPUT_DIR = 'EBCodeSearch/Data'

# 日志文件目录
LOG_FILE = "EBCodeSearch/Log/{}.log".format(time.strftime("%Y-%m-%d", time.localtime()))

# 日志级别，默认为DEBUG
# LOG_LEVEL = "WARNING"

# 新的启动命令，用于一次启动所有spider
COMMANDS_MODULE = 'EBCodeSearch.commands'

# 要爬取的关键字
# KEY_WORDS = [
#     ['Python', '这里是关于第一个关键字的描述'],
#     ['JAVA', "这里是关于第二个关键字的描述"]
# ]
KEY_WORDS_DETAIL = collections.OrderedDict()

VALID_WORDS = set()

# result count
GITHUB_COUNT = 0
GITEE_COUNT = 0
GITLAB_COUNT = 0

RESULT_DETAIL = {
    'name' : '用户名',
    'private' : '仓库是否私有',
    'user_url' : '用户主页',
    'repo_url' : '仓库主页',
    'description' : '仓库描述',
    'created_at' : '仓库创建时间',
    'updated_at' : '仓库更新时间'
}

# Gitlab private token
GITLAB_PRIVATE_TOKEN = 'ZW9v-iPAqCsWzdQRqecZ'

###################
# Email Configure #
###################

# 邮箱账号，用于发送邮件
EMAIL_USER = "spider_sender@126.com"

# 邮箱密码或者授权码，126邮箱使用的为授权码，密码为`123456qwer`
EMAIL_PASSWORD = "RFQRKKYMLDUTLPNV"

# 邮箱服务器地址
EMAIL_SERVER = "smtp.126.com"

# 邮件收件人，多个收件人使用列表，收件人只有一人时可以直接设置`TO = "xxxx@xx.xx"`
TO = ["zhuweijie@ebupt.com"]
