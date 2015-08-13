from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView
from .models import Site


class IndexView(generic.ListView):
	template_name = 'webapp/index.html'
	context_object_name = 'site_list'

	def get_queryset(self):
		return Site.objects.order_by('name')
