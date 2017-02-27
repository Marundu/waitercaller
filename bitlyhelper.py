import json
import urllib2

TOKEN='4c760990f32e0bd01b5cf8b753cb63a643016954'
ROOT_URL='https://api-ssl.bitly.com/'
SHORTEN='/v3/shorten?access_token={}&longUrl={}'

class BitlyHelper:
	def shorten_url(self, longurl):
		try:
			url=ROOT_URL + SHORTEN.format(TOKEN, longurl)
			response=urllib2.urlopen(url).read()
			jr=json.loads(response)
			return jr['data']['url']
		except Exception as e:
			print e
