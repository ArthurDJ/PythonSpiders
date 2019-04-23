# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class WikileaksPipeline(object):
    def __init__(self):
        path = './cxynb'
        if not os.path.exists(path):
            os.mkdir(path)
            self.path = path
        else:
            self.path = path

    def process_item(self, item, spider):
        file = dict(item)
        file_name = '/' + file['file_name']
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        with open(self.path + "/" + file["file_name"], 'wb') as f:
            f.write(file["file_content"])
            f.close()
        return item
