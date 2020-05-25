#-*- coding: utf-8 -*-
import sys
if len(sys.argv)>1 and sys.argv[1] is not None:
    sys.path.append(sys.argv[1])

import paho.mqtt.client as mqtt
from find.pushwx import pushwx

import traceback

MQTT_URI='mqtt.eclipse.org'
MQTT_PORT=1883
MQTT_CLIENT='new_game'
MQTT_SUBSCRIPTION='newgame'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_SUBSCRIPTION)         # 订阅消息


def on_message(client, userdata, msg):
    #print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))
    try:
        ms = eval(msg.payload)
        print(ms)
        rc = pushwx.send_msg(ms)
        print('微信消息发的结果是： ',rc)
    except Exception as e :
        traceback.print_exc()


def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)




pushwx = pushwx()
mqtt_client = mqtt.Client(MQTT_CLIENT)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_disconnect = on_disconnect
mqtt_client.connect(host=MQTT_URI, port=MQTT_PORT, keepalive=60)
mqtt_client.loop_forever()