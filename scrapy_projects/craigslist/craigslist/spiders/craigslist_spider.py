import scrapy
from craigslist.items import CraigslistItem

class CraigslistSpider(scrapy.Spider):
	name = "craigslist"
	allowed_domains = ["craigslist.org"]
	start_urls = [
	"http://sfbay.craigslist.org/search/sfc/apa"
	]

	def parse(self, response):
		# filename = response.url.split("/")[-2]
		# with open(filename, 'wb') as f:
		# 	f.write(response.body)
		for sel in response.xpath("//a[@class='hdrlnk']"):

			item = CraigslistItem()
			item['title'] =  sel.xpath("span[@id='titletextonly']").extract()[0]
			item['link']  =  sel.xpath("span/span/a[@class='hdrlnk']/@href").extract()[0]
			yield item