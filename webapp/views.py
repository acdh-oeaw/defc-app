from django.shortcuts import render, render_to_response
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView
from .models import Site

#views for Site
class SiteCreate(CreateView):
	model = Site
	fields = "__all__"
	
	
class SiteUpdate(UpdateView):
		model = Site
		fields = "__all__"
		template_name_suffix = '_update_form'

#	<!--<a href="{% url 'webapp:site_update' %} {{ site.id_site }}">{{ site.name }}</a>--> creates an error

	
class IndexView(generic.ListView):
	template_name = 'webapp/sites.html'
	context_object_name = 'site_list'

	def get_queryset(self):
		return Site.objects.order_by('name')




		

def start_view(request):
	return render_to_response('webapp/index.html')