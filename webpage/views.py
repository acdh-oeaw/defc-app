from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Event

# Create your views here.
def homepage(request):
	context = RequestContext(request)
	return render(request, 'webpage/index.html', context)


def about(request):
	#context = RequestContext(request)
	context = {}
	context["event_list"] = Event.objects.all()
	return render(request, 'webpage/about.html', context)



class EventListViewAdmin(generic.ListView):
	template_name = 'webpage/event_list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return Event.objects.all()


class EventCreate(CreateView):
	model = Event
	fields = "__all__"
	template_name = "webpage/create_event.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(EventCreate, self).dispatch(*args, **kwargs)


class EventDelete(DeleteView):
	model = Event
	template_name = 'defcdb/confirm_delete.html'
	success_url = reverse_lazy('webpage:event_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(EventDelete, self).dispatch(*args, **kwargs)