import requests
import rss


class LoginService:
    def doLogin(self):
        postdata =  {'username': rss.USERNAME,
            'password': rss.PASSWORD,
            'questionid': rss.QUESTIONID,
            'answer': rss.ANSWER,
            'refer':rss.REFER
            }
        session = requests.session()
        session.get(rss.INDEX_URL, headers=rss.HEADERS)
        response = session.post(rss.LOGIN_URL, postdata)
        if 200 == response.status_code:
            return session
        else:
            raise Exception('login error!')
