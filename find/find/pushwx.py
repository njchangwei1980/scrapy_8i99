#-*- coding: utf-8 -*-
import json
import requests
import urllib
from find.items import GameItem


class pushwx:
    def __init__(self):
        wechat_config = {
            'appid': 'wx07ea3408f1a7c3c5',  # (No.1)此处填写你的appid
            'appsecret': '06dc7456e1bde64ae8c85cdf43ded338',  # (No.2)此处填写你的appsecret
            'template_id': 'XNLmm-88jJGYVpQTW1KEsCfB3sx4VOommWnzrKzlnMI'  # (No.3)此处填写你的模板消息ID
        }
        self.appid = wechat_config['appid']
        self.appsecret = wechat_config['appsecret']
        self.template_id = wechat_config['template_id']
        self.access_token = ''
        self.openid = {'openid':'oUAGW1I5N6rvJuxAgFThoP-TQ7sY'}

    def get_access_token(self, appid, appsecret):
        # url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' \
        #       % (str(appid), str(appsecret))
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' \
                % (str(appid), str(appsecret))
        request = requests.get(url)
        data = json.loads(request.text)
        access_token = data['access_token']
        self.access_token = access_token
        return self.access_token

    def send_msg(self,  item):
        msg = {
            'touser': self.openid['openid'],
            'template_id': self.template_id,
            'data': {
                'title': {
                    'value': item['title'],
                    'color': '#0000CD'
                },
                'language': {
                    'value': item['language'],
                },
                'type': {
                    'value': item['type'],
                },
                'form': {
                    'value': item['form'],
                },
                'sellingtime': {
                    'value': item['sellingtime'],
                },
                'updatetime': {
                    'value': item['updatetime'],
                }
            }
        }
        json_data = json.dumps(msg)
        if self.access_token == '':
            self.get_access_token(self.appid, self.appsecret)
        access_token = self.access_token
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % str(access_token)
        r = requests.post(url, json_data)
        return json.loads(r.text)


if __name__ == '__main__':
    # 微信配置
    wechat_config = {
        'appid': 'wx07ea3408f1a7c3c5',  # (No.1)此处填写你的appid
        'appsecret': '06dc7456e1bde64ae8c85cdf43ded338',  # (No.2)此处填写你的appsecret
        'template_id': 'XNLmm-88jJGYVpQTW1KEsCfB3sx4VOommWnzrKzlnMI'  # (No.3)此处填写你的模板消息ID
    }

    # 用户列表
    openid = {'openid':'oUAGW1I5N6rvJuxAgFThoP-TQ7sY'}

    # 执行
    icb = pushwx(wechat_config)

    item = {'title':'newgame', 'language':'中文', 'type':'动作', 'form':'xci', 'sellingtime':'2020-5-11', 'updatetime':'2020-5-11'}

    rt = icb.send_msg(item)

    print(rt)
