from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from .models import ImageThesaurus
# Create your views here.



class ImageThesaurusListView(generic.ListView):
	model = ImageThesaurus
	template_name = 'images_metadata/image_gallery.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return ImageThesaurus.objects.all()




