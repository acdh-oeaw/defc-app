from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Contact, Project, Threedmodel
from defcdb.models import Finds
from .forms import ThreedmodelForm
# Create your views here.

class ThreedmodelListView(generic.ListView):
    model = Threedmodel
    template_name = 'threedmodels/3dmodels_list.html'
    # template_name = 'images_metadata/public_image_gallery.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Threedmodel.objects.all()


class ThreedmodelDetail(DetailView):
    model = Threedmodel
    template_name = 'threedmodels/3dmodels_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ThreedmodelDetail, self).get_context_data(**kwargs)
        current_object = self.object
        context['inclusion_list'] = current_object.inclusion.all()
        #context['region_list'] = current_object.region.all()
        #context['region_list'] = DC_region.objects.filter(imagethesaurus=current_object.id)
        # context['institution_list'] = current_object.institution.all()
        # context['specialanalysis_list'] = current_object.special_analysis.all()
        # context['reference_list'] = current_object.reference.all()
        # context['finds_list'] = Finds.objects.filter(research_event=current_object.id)
        return context


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = ThreedmodelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('threedmodels:object_list')
        else:
            return render(request, 'threedmodels/create_virtualobject.html', {'form': form})
    else:
        form = ThreedmodelForm()
    return render(request, 'threedmodels/create_virtualobject.html', {'form': form})


@login_required
def update_file(request, pk):
    instance = get_object_or_404(Threedmodel, id=pk)
    if request.method == 'POST':
        form = ThreedmodelForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('threedmodels:object_list')
        else:
            return render(request, 'threedmodels/create_virtualobject.html', {'form': form})
    else:
        form = ThreedmodelForm(instance=instance)
    return render(request, 'threedmodels/create_virtualobject.html', {'form': form})