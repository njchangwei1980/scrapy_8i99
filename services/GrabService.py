import rss


class GrabService:
    def getContent(self, session):
        response = session.get(rss.MAIN_URL)
        if 200 == response.status_code:
            return response.content
        else:
            raise Exception('Grab Url error!,url=%s', rss.MAIN_URL)
