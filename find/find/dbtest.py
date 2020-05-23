#-*- coding: utf-8 -*-
# from pymongo import MongoClient
#
#
# connect = MongoClient(host='mongodb+srv://cluster0-9vjnw.mongodb.net/test',username='njchangwei',password='19800121')
#
# db = connect['games']
# collection = db['games']
#
# query = {'title':'北方之魂1'}
#
# print(collection.count_documents(query))

# import paho.mqtt.client as mqtt
#
# MQTT_URI='mqtt.eclipse.org'
# MQTT_PORT=1883
# MQTT_CLIENT='new_game'
# MQTT_SUBSCRIPTION='newgame'
#
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#     client.subscribe(MQTT_SUBSCRIPTION)         # 订阅消息
#
#
# def on_message(client, userdata, msg):
#     print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))
#
#
# def on_subscribe(client, userdata, mid, granted_qos):
#     print("On Subscribed: qos = %d" % granted_qos)
#
#
# def on_disconnect(client, userdata, rc):
#     if rc != 0:
#         print("Unexpected disconnection %s" % rc)
#
#
# mqtt_client = mqtt.Client(MQTT_CLIENT)
# mqtt_client.on_connect = on_connect
# mqtt_client.on_message = on_message
# mqtt_client.on_subscribe = on_subscribe
# mqtt_client.on_disconnect = on_disconnect
# mqtt_client.connect(host=MQTT_URI, port=MQTT_PORT, keepalive=600)
# mqtt_client.publish(MQTT_SUBSCRIPTION,'ok ,good111',0)
# mqtt_client.loop_forever()


import sys
import os



if sys.argv[1] is not None:
    print(sys.argv[1])
    path = sys.argv[1]

print(os.path)