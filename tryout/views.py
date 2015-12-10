from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from .forms import AreaTryForm
from .models import AreaTry
from defcdb.models import DC_period_datingmethod, DC_period_datedby


class AreaTryListView(generic.ListView):
	template_name = 'tryout/areatry_list.html'
	context_object_name = 'object_list' 

	def get_queryset(self):
		return AreaTry.objects.order_by('site')


def create_area(request):
	if request.method == "POST":
		form = AreaTryForm(request.POST)
		if form.is_valid():
			new_area = form.save()
			return redirect('tryout:areatry_detail', pk=new_area.id)
	else:
		form = AreaTryForm()
		return render(request, 'tryout/create_areatry.html', {'form':form})


class AreaTryDetail(DetailView):
	model = AreaTry
	def get_context_data(self, **kwargs):
		context = super(AreaTryDetail, self).get_context_data(**kwargs)
		current_area = self.object
	

		return context