from lxml import etree

class WrapService:
    def doWrapGames(self,html_content):
        html = etree.HTML(html_content)
        items = html.xpath("//div[@class='nex_sologame_list_title']/a/text()")
        print(len(items))