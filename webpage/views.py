from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Event


# Create your views here.
def imprint(request):
    context = RequestContext(request)
    return render(request, "webpage/imprint.html")


def homepage(request):
    context = RequestContext(request)
    return render(request, "webpage/index.html")


def about(request):
    # context = RequestContext(request)
    context = {}
    context["event_list"] = Event.objects.all()
    return render(request, "webpage/about.html", context=context)


def terms_of_use(request):
    context = RequestContext(request)
    return render(request, "webpage/terms_of_use.html")


def cukurici_movie_content(request):
    context = RequestContext(request)
    return render(request, "webpage/cukurici_movie_content.html")


def cukurici_movie_german_version(request):
    context = RequestContext(request)
    return render(request, "webpage/cukurici_movie_german_version.html")


def ada_tepe_movie_content(request):
    context = RequestContext(request)
    return render(request, "webpage/ada_tepe_movie_content.html")


def ada_tepe_movie_german_version(request):
    context = RequestContext(request)
    return render(request, "webpage/ada_tepe_movie_german_version.html")


def blog_main(request):
    context = RequestContext(request)
    return render(request, "webpage/blog_main.html")


def blog_post_01(request):
    context = RequestContext(request)
    return render(request, "webpage/blog_post_01.html")


def blog_post_02(request):
    context = RequestContext(request)
    return render(request, "webpage/blog_post_02.html")


def blog_post_03(request):
    context = RequestContext(request)
    return render(request, "webpage/blog_post_03.html")


def blog_post_04(request):
    context = RequestContext(request)
    return render(request, "webpage/blog_post_04.html")


def blog_post_05(request):
    context = RequestContext(request)
    return render(request, "webpage/blog_post_05.html")


def defc2rdf_demo(request):
    context = RequestContext(request)
    return render(request, "webpage/defc2rdf_demo.html")


def mapping2cidoc(request):
    context = RequestContext(request)
    return render(request, "webpage/mapping2cidoc.html")


def defc_thesaurus(request):
    context = RequestContext(request)
    return render(request, "webpage/defc_thesaurus.html")


def chronology_table(request):
    context = RequestContext(request)
    return render(request, "webpage/chronology_table.html")


class EventListViewAdmin(generic.ListView):
    template_name = "webpage/event_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        return Event.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventListViewAdmin, self).dispatch(*args, **kwargs)


class EventCreate(CreateView):
    model = Event
    fields = "__all__"
    template_name = "webpage/create_event.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventCreate, self).dispatch(*args, **kwargs)


class EventUpdate(UpdateView):
    model = Event
    fields = "__all__"
    template_name = "webpage/update_event.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventUpdate, self).dispatch(*args, **kwargs)


class EventDelete(DeleteView):
    model = Event
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("webpage:event_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventDelete, self).dispatch(*args, **kwargs)
