# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class EbcodesearchItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class GithubItem(scrapy.Item):
    name = scrapy.Field()        # 用户名
    private = scrapy.Field()     # 仓库是否私有
    user_url = scrapy.Field()    # 用户主页
    repo_url = scrapy.Field()    # 仓库主页
    description = scrapy.Field() # 仓库描述
    created_at = scrapy.Field()  # 仓库创建时间
    updated_at = scrapy.Field()  # 仓库更新时间


class GiteeItem(scrapy.Item):
    name = scrapy.Field()         # 用户名
    private = scrapy.Field()      # 仓库是否私有
    user_url = scrapy.Field()     # 用户主页
    repo_url = scrapy.Field()     # 仓库主页
    description = scrapy.Field()  # 仓库描述
    created_at = scrapy.Field()   # 仓库创建时间
    updated_at = scrapy.Field()   # 仓库更新时间


class GitlabItem(scrapy.Item):
    name = scrapy.Field()         # 用户名
    user_url = scrapy.Field()     # 用户主页
    repo_url = scrapy.Field()     # 仓库主页
    description = scrapy.Field()  # 仓库描述
    created_at = scrapy.Field()   # 仓库创建时间
    updated_at = scrapy.Field()   # 仓库更新时间
