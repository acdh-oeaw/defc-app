import requests, json, sys
from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Book
# following line has to match the settings-file you are using
from orea.settings.server import Z_USER_ID, Z_COLLECTION, Z_API_KEY 


def sync_zotero(request):
    context = {'context': [{"hansi":"hansi is a name"},{"biene maya":"is a bee"}]}
    return render(request, 'bib/synczotero.html', context)

@login_required
def sync_zotero_action(request):
	root = "https://api.zotero.org/users/"
	params = "{}/collections/{}/items/top?v=3&key={}".format(Z_USER_ID,Z_COLLECTION,Z_API_KEY)
	url = root+params+"&sort=dateModified&limit=10"
	books_before = len(Book.objects.all())
	try:
		r = requests.get(url)
		error = "No errors from ZoteroAPI"
	except:
		error = "aa! errors! The API didn´t response with a proper json-file"

	response = r.json()
	failed = []
	saved = []
	for x in response:
		try:
			x["data"]["creators"][0]["name"]
			NewBook = Book(zoterokey = x["data"]["key"],
		                      item_type =x["data"]["itemType"],
		                      author=x["data"]["creators"][0]["name"],
		                      title =x["data"]["title"],
		                      short_title = x["data"]["shortTitle"])
		except:
			x["data"]["creators"] = "no author provided"

			NewBook = Book(zoterokey = x["data"]["key"],
		                      item_type =x["data"]["itemType"],
		                      author=x["data"]["creators"],
		                      title =x["data"]["title"],
		                      short_title = x["data"]["shortTitle"])
		try:
		    NewBook.save()
		    saved.append(x['data'])
		except:
		    failed.append(x['data'])
	books_after = len(Book.objects.all())
	context = {}
	context["error"] = error
	context["saved"] = saved
	context["failed"] = failed
	context["books_before"] = [books_before]
	context["books_after"] = [books_after]
	return render(request, 'bib/synczotero_action.html', context)
