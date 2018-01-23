from lxml import html, etree, cssselect
import requests, re, pymongo
from pymongo import MongoClient

client = MongoClient()
client.drop_database("pfoundation_data")
db = client.pfoundation_data
poems = db.poems

n = 0
poem_number = 0
while n <= 166:
	n = n + 1
	payload = {'filter_poetry_first': '1', 'page': n }
	page = requests.get('http://www.poetryfoundation.org/searchresults?', params=payload)
	tree = html.fromstring(page.text)
	links = tree.xpath('//p/a/@href')
	print (n)
	print (links)
	for url in links:
		poem_number = poem_number + 1
		poem_url = 'http://poetryfoundation.org' + url
		poem = requests.get(poem_url)
		poem_tree = html.fromstring(poem.text)
		title = poem_tree.xpath('//*[@id="poem-top"]/h1/text()')
		author = poem_tree.xpath('//*[@id="poemwrapper"]/span[1]/a/text()')
		author_link = poem_tree.xpath('//*[@id="poemwrapper"]/span[1]/a/@href')
		translator = poem_tree.xpath('//*[@id="poemwrapper"]/p[@class="translated"]/span/a/text()')
		translator_link = poem_tree.xpath('//*[@id="poemwrapper"]/p[@class="translated"]/span/a/@href')

		poem_html = poem_tree.cssselect('div.poem')
		poem_text = ""
		for line in poem_html:
			poem_text = poem_text + html.tostring(line)

		credit = poem_tree.xpath('//*[@id="poem"]/div[@class="credit"]/p/text()')

		#print (url)
		#print (title)
		#print (author)
		#print (author_link)
		#print (translator)
		#print (translator_link)
		#print (poem_text)
		#print (credit)

		poem = {
			"number" : poem_number,
			"url" : url,
			"title" : title,
			"author" : author,
			"author_link" : author_link,
			"translator" : translator,
			"translator_link" : translator_link,
			"poem_text" : poem_text,
			"credit" : credit
		}

		poem_id = poems.insert_one(poem).inserted_id
		print (`poem_number` + " " + `poem_id`)