from lxml import etree
import json
import Scraper


url = "https://www.justdial.com/Ahmedabad/Karvy-Stock-Broking-Ltd-Beside-Associated-Petrol-Pump-C-G-Road/079PXX79-XX79-000819424881-F9I5_BZDET?xid=QWhtZWRhYmFkIHN0b2NrIGJyb2tpbmc="
#Web = Scraper.Web_Scraper()
#html = Web.get_html_one(url)


class Parser():

    def get_columns(self, html):
        tree = etree.HTML(html)
        scripts = tree.xpath('.//script[@type="application/ld+json"]')[1].xpath('.//text()')[0]
        scripts_dic = json.loads(scripts)
        name = scripts_dic['name']
        web_site_object = tree.xpath('.//span[@class="mreinfp comp-text"]/a')
        if len(web_site_object) == 2:
            web_site = web_site_object[1].xpath('.//@href')[0]
        else:
            web_site = ""
        adress = tree.xpath('.//span[@class="lng_add"]')[2].xpath('.//text()')[0]
        telephone_object = tree.xpath('.//a[@class="tel"]')
        if len(telephone_object) == 3:
            telephone = telephone_object[0].xpath('.//text()')[0]
        else:
            telephone = telephone_object[0].xpath('.//text()')[0] \
                        + ", " + telephone_object[1].xpath('.//text()')[0]


        print(web_site)
        print(adress)
        print(telephone)
        print(name)

    def get_url_topic(self, html):
        tree = etree.HTML(html)
        urls = tree.xpath('.//li[@class="cntanr"]/@data-href')
        print(urls)
        print(len(urls))


P = Parser()
f=open('1.txt','r', encoding="utf-8")
html = f.read()
P.get_url_topic(html)