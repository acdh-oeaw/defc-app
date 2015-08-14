from django.http import HttpResponse
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse, reverse_lazy

from .models import Site, Settlement, Finds
from .forms import *

#################################################################
#				views for login/logout							#
#################################################################
def user_login(request):
	errors=[]
	if request.method == 'POST':
		form = form_user_login(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(request.GET.get('next','/webapp/'))
				else:
					return HttpResponse('not active.')
			else:
				return HttpResponse('user does not exist')
	else:
		form = form_user_login()
		return render(request, 'webapp/user_login.html', {'form':form})


def user_logout(request):
	logout(request)
	return render_to_response('webapp/logout.html')

#################################################################
#				views for Site									#
#################################################################
class SiteListView(generic.ListView):
	template_name = 'webapp/site_list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return Site.objects.order_by('name')


class SiteCreate(CreateView):
	model = Site
	fields = "__all__"
	template_name = "webapp/create_form.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteCreate, self).dispatch(*args, **kwargs)

	
class SiteUpdate(UpdateView):
	model = Site
	fields = "__all__"
	template_name = 'webapp/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteUpdate, self).dispatch(*args, **kwargs)


class SiteDelete(DeleteView):
	model = Site
	template_name = 'webapp/confirm_delete.html'
	success_url = reverse_lazy('webapp:site_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteDelete, self).dispatch(*args, **kwargs)


class SiteDetail(DetailView):
	model = Site
	def get_context_data(self, **kwargs):
		context = super(SiteDetail, self).get_context_data(**kwargs)
		return context


#################################################################
#				views for Finds									#
#################################################################

class FindsListView(generic.ListView):
	template_name = 'webapp/finds_list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return Finds.objects.order_by('finds_type')


class FindsCreate(CreateView):
	model = Finds
	fields = "__all__"
	template_name = "webapp/create_form.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(FindsCreate, self).dispatch(*args, **kwargs)


class FindsUpdate(UpdateView):
	model = Finds
	fields = "__all__"
	template_name = 'webapp/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(FindsUpdate, self).dispatch(*args, **kwargs)


class FindsDelete(DeleteView):
	model = Finds
	template_name = 'webapp/confirm_delete.html'
	success_url = reverse_lazy('webapp:finds_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(FindsDelete, self).dispatch(*args, **kwargs)


class FindsDetail(DetailView):
	model = Finds
	def get_context_data(self, **kwargs):
		context = super(FindsDetail, self).get_context_data(**kwargs)
		return context


#################################################################
#				views for Finds									#
#################################################################

class SettlementListView(generic.ListView):
	template_name = 'webapp/settlement_list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return Settlement.objects.order_by('settlement_type')


class SettlementCreate(CreateView):
	model = Settlement
	fields = "__all__"
	template_name = "webapp/create_form.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SettlementCreate, self).dispatch(*args, **kwargs)


class SettlementUpdate(UpdateView):
	model = Settlement
	fields = "__all__"
	template_name = 'webapp/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SettlementUpdate, self).dispatch(*args, **kwargs)


class SettlementDelete(DeleteView):
	model = Settlement
	template_name = 'webapp/confirm_delete.html'
	success_url = reverse_lazy('webapp:settlement_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SettlementDelete, self).dispatch(*args, **kwargs)


class SettlementDetail(DetailView):
	model = Settlement
	def get_context_data(self, **kwargs):
		context = super(SettlementDetail, self).get_context_data(**kwargs)
		return context



#################################################################
#				basic application views							#
#################################################################


def start_view(request):
	context = RequestContext(request)
	return render(request, 'webapp/index.html', context)

