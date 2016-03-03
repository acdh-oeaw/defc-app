import requests, json, sys
from django.core.management.base import NoArgsCommand

import requests, json, sys
from bib.models import Book
from orea.settings.server import Z_USER_ID, Z_COLLECTION, Z_API_KEY


class Command(NoArgsCommand):
	help = "a simple script to sync defc-db with zotero"
	def handle_noargs(self, **options):
		root = "https://api.zotero.org/users/"
		params = "{}/collections/{}/items/top?v=3&key={}".format(Z_USER_ID,
		                                                         Z_COLLECTION,
		                                                         Z_API_KEY)
		url = root+params+"&sort=dateModified&limit=100"
		try:
		    r = requests.get(url)
		except:
		    sys.exit("aa! errors! The API didn´t response with a proper json-file")

		response = r.json()

		failed = []
		saved = []
		for x in response:
		    NewBook = Book(zoterokey = x["data"]["key"],
		                      item_type =x["data"]["itemType"],
		                      author=x["data"]["creators"][0]["name"],
		                      title =x["data"]["title"],
		                      short_title = x["data"]["shortTitle"])
		    try:
		        NewBook.save()
		        saved.append(x['data'])
		    except:
		        failed.append(x['data'])
		print('saved: {} objects \nfailed: {} objects'.format(len(saved), len(failed)))