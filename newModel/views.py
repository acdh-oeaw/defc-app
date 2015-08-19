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

from .models import Site, Area
from .forms import form_user_login

#################################################################
#				views for Site									#
#################################################################
class SiteListView(generic.ListView):
	template_name = 'newModel/list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return Site.objects.order_by('name')


class SiteCreate(CreateView):
	model = Site
	fields = "__all__"
	template_name = "newModel/create_form.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteCreate, self).dispatch(*args, **kwargs)


class SiteUpdate(UpdateView):
	model = Site
	fields = "__all__"
	template_name = 'newModel/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteUpdate, self).dispatch(*args, **kwargs)


class SiteDelete(DeleteView):
	model = Site
	template_name = 'newModel/confirm_delete.html'
	success_url = reverse_lazy('newModel:site_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteDelete, self).dispatch(*args, **kwargs)


class SiteDetail(DetailView):
	model = Site
	def get_context_data(self, **kwargs):
		context = super(SiteDetail, self).get_context_data(**kwargs)
		return context

#################################################################
#				views for Area									#
#################################################################
class AreaListView(generic.ListView):
	template_name = 'newModel/list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return Area.objects.order_by('area_type')


class AreaCreate(CreateView):
	model = Area
	fields = "__all__"
	template_name = "newModel/create_form.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AreaCreate, self).dispatch(*args, **kwargs)


class AreaUpdate(UpdateView):
	model = Area
	fields = "__all__"
	template_name = 'newModel/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AreaUpdate, self).dispatch(*args, **kwargs)


class AreaDelete(DeleteView):
	model = Area
	template_name = 'newModel/confirm_delete.html'
	success_url = reverse_lazy('newModel:area_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AreaDelete, self).dispatch(*args, **kwargs)


class AreaDetail(DetailView):
	model = Area
	def get_context_data(self, **kwargs):
		context = super(AreaDetail, self).get_context_data(**kwargs)
		return context
		
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
					return HttpResponseRedirect(request.GET.get('next','/newModel/'))
				else:
					return HttpResponse('not active.')
			else:
				return HttpResponse('user does not exist')
	else:
		form = form_user_login()
		return render(request, 'newModel/user_login.html', {'form':form})


def user_logout(request):
	logout(request)
	return render_to_response('newModel/logout.html')

#################################################################
#				basic application views							#
#################################################################


def start_view(request):
	context = RequestContext(request)
	return render(request, 'newModel/index.html', context)

