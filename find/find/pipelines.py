# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
from pymongo import MongoClient
import paho.mqtt.client as mqtt
import json

MONGO_URI='mongodb+srv://cluster0-9vjnw.mongodb.net/test'
MONGO_USER_NAME = 'njchangwei'
MONGO_PASSWORD = '19800121'
MONGO_DB = 'games'
MONGO_DB_COLLECTION = 'games'

MQTT_URI='mqtt.eclipse.org'
MQTT_PORT=1883
MQTT_CLIENT='newgame'
MQTT_SUBSCRIPTION='newgame'

class FindPipeline(object):
    def process_item(self, item, spider):
        return item

class GamePipeline(object):
    def __init__(self):
        self.fp = open('games.json','wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    def process_item(self,item,spider):

        if len(item['language'][0].split("："))>1:
            item['language'] = item['language'][0].split("：")[1]

        if len(item['sellingtime'][0].split("：")) > 1:
            item['sellingtime'] = item['sellingtime'][0].split("：")[1]

        if len(item['type'][0].split("：")) > 1:
            item['type'] = item['type'][0].split("：")[1]

        if len(item['updatetime'][0].split("：")) > 1:
            item['updatetime'] = item['updatetime'][0].split("：")[1]

        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.fp.close()

class GameMongoPipeline(object):
    def __init__(self):
        self.mongo_uri = MONGO_URI
        self.mongo_user_name = MONGO_USER_NAME
        self.mongo_password = MONGO_PASSWORD
        self.mongo_db = MONGO_DB
        self.mqtt_client = mqtt.Client(MQTT_CLIENT)
        self.mqtt_client.connect(host=MQTT_URI,port=MQTT_PORT,keepalive=60)


    def open_spider(self,spider):
        self.client = MongoClient(host=self.mongo_uri,username=self.mongo_user_name,password=self.mongo_password)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[MONGO_DB_COLLECTION]

    def process_item(self, item, spider):

        query_data = {'title':item['title']}
        if self.collection.count_documents(query_data) == 0:
            if len(item['language'][0].split("："))>1:
                item['language'] = item['language'][0].split("：")[1]

            if len(item['sellingtime'][0].split("：")) > 1:
                item['sellingtime'] = item['sellingtime'][0].split("：")[1]

            if len(item['type'][0].split("：")) > 1:
                item['type'] = item['type'][0].split("：")[1]

            if len(item['updatetime'][0].split("：")) > 1:
                item['updatetime'] = item['updatetime'][0].split("：")[1]

            data = dict(item)
            self.collection.insert(data)
            self.mqtt_client.publish(MQTT_SUBSCRIPTION,str(item),0)
        return item

    def close_spider(self,spider):
        self.client.close()

    def push_to_mqtt(self,item):
        pass
