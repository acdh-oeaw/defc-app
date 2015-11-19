# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import VirtualObject
from .forms import VirtualObjectForm

@login_required
def upload_file(request):
	if request.method == 'POST':
		form = VirtualObjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('virtualgallery:list')
	else:
		form = VirtualObjectForm()
	return render(request, 'virtualgallery/create_virtualobject.html', {'form':form})


class VirtualObjectListView(generic.ListView):
	model = VirtualObject
	template_name = 'virtualgallery/list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return VirtualObject.objects.order_by('id')


class VirtualObjectDetail(DetailView):
	model = VirtualObject
	def get_context_data(self, **kwargs):
		context = super(VirtualObjectDetail, self).get_context_data(**kwargs)
		current_object = self.object
		return context


