from lxml import etree
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor

#class Parser():

   # def get_culuns(self, html):
       # tree = etree.HTML(html)

data = """
{
    "@context": "http://schema.org",
    "@type": "LocalBusiness",
    "url": "https://www.justdial.com/Ahmedabad/Karvy-Stock-Broking-Ltd-Beside-Associated-Petrol-Pump-C-G-Road/079PXX79-XX79-000819424881-F9I5_BZDET?xid=QWhtZWRhYmFkIHN0b2NrIGJyb2tpbmc=",
    "name": "Karvy Stock Broking Ltd",
    "image": "https://content.jdmagicbox.com/ahmedabad/i5/079pxx79.xx79.000819424881.f9i5/catalogue/karvy-stock-broking-ltd-c-g-road-ahmedabad-l77ta.jpg",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "",
        "addressLocality": "403, 4th Floor, Samedh Complex, C G Road",
        "postalCode": "380009",
        "addressRegion": "Ahmedabad"
    }
    ,
    "telephone": ["+917967772603","+917967772600"],
            
	"aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "3.9",
        "ratingCount": "212"
    	},
    
	"review": [
        {
            "@type": "Review",
            "datePublished": "2017-07-11 16:33:36",
            "reviewBody": "Excellent",
            "author": {
                "@type": "Person",
                "name": "Kintan"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-07-03 15:10:27",
            "reviewBody": "Excellent",
            "author": {
                "@type": "Person",
                "name": "Jayant C.patel"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-06-28 15:54:54",
            "reviewBody": "Very Good",
            "author": {
                "@type": "Person",
                "name": "Mr Bhavin Patel"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-05-16 18:03:04",
            "reviewBody": "Very Good",
            "author": {
                "@type": "Person",
                "name": "Mr Jatin Thakkar"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-04-06 11:53:04",
            "reviewBody": "Excellent",
            "author": {
                "@type": "Person",
                "name": "Mr Hemal Mehta"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-04-03 10:13:30",
            "reviewBody": "Excellent",
            "author": {
                "@type": "Person",
                "name": "Mr Maulik"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-03-29 13:08:18",
            "reviewBody": "Excellent",
            "author": {
                "@type": "Person",
                "name": "Mr Jitendra"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-02-15 15:49:48",
            "reviewBody": "Excellent",
            "author": {
                "@type": "Person",
                "name": "Mr Jignesh Gohil"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-02-11 10:25:25",
            "reviewBody": "Excellent",
            "author": {
                "@type": "Person",
                "name": "Ms Sonal Singh"
            }
        },
        {
            "@type": "Review",
            "datePublished": "2017-01-12 21:30:45",
            "reviewBody": "Good",
            "author": {
                "@type": "Person",
                "name": "Rajendra Rajput"
            }
        }
	]
	    ,
    "paymentAccepted": ["Cheques"],
    "openingHoursSpecification": [ {
				  "@type": "OpeningHoursSpecification",
				  "dayOfWeek": "http://schema.org/Monday ",
				  "opens": [" 09:30 am "],
				  "closes": [" 05:30 pm"] },{
				  "@type": "OpeningHoursSpecification",
				  "dayOfWeek": "http://schema.org/Tuesday ",
				  "opens": [" 09:30 am "],
				  "closes": [" 05:30 pm"] },{
				  "@type": "OpeningHoursSpecification",
				  "dayOfWeek": "http://schema.org/Wednesday ",
				  "opens": [" 09:30 am "],
				  "closes": [" 05:30 pm"] },{
				  "@type": "OpeningHoursSpecification",
				  "dayOfWeek": "http://schema.org/Thursday ",
				  "opens": [" 09:30 am "],
				  "closes": [" 05:30 pm"] },{
				  "@type": "OpeningHoursSpecification",
				  "dayOfWeek": "http://schema.org/Friday ",
				  "opens": [" 09:30 am "],
				  "closes": [" 05:30 pm"] },{
				  "@type": "OpeningHoursSpecification",
				  "dayOfWeek": "http://schema.org/Saturday ",
				  "opens": [" 09:30 am "],
				  "closes": [" 03:30 pm"] }],
    "logo": [ "https://images.jdmagicbox.com/upload_test/mumbai/t4/022pxx22.xx22.100106162949.e6t4/logo/f85b3802612a5a6abbe2cc851d2d3fc4.jpg"]    ,
    "photos":{"@type": "ImageObject","url": [ "https://content2.jdmagicbox.com/ahmedabad/i5/079pxx79.xx79.000819424881.f9i5/catalogue/karvy-stock-broking-ltd-c-g-road-ahmedabad-l77ta.jpg",""]}}

"""

parser = Parser()
tree = parser.parse(data)
fields = {getattr(node.left, 'value', ''): getattr(node.right, 'value', '')
          for node in nodevisitor.visit(tree)
          if isinstance(node, ast.Assign)}