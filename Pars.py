from lxml import etree
import json
import Scraper


url = "https://www.justdial.com/Ahmedabad/Karvy-Stock-Broking-Ltd-Beside-Associated-Petrol-Pump-C-G-Road/079PXX79-XX79-000819424881-F9I5_BZDET?xid=QWhtZWRhYmFkIHN0b2NrIGJyb2tpbmc="
Web = Scraper.Web_Scraper()
html = Web.get_html(url)
print(html)

class Parser():

    def get_culuns(self, html):
        tree = etree.HTML(html)
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

P = Parser()
P.get_culuns(html)