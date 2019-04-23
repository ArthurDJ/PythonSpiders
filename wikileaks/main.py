# -*- coding:utf-8 -*-
from scrapy import cmdline
cmdline.execute('scrapy crawl file'.split())

# cmdline.execute('scrapy crawl file -o file.json'.split())