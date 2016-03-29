from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from .models import ImageThesaurus
from .forms import ImageThesaurusForm


class ImageThesaurusListView(generic.ListView):
    model = ImageThesaurus
    template_name = 'images_metadata/image_gallery.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return ImageThesaurus.objects.all()


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = ImageThesaurusForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_gallery:object_list')
        else:
            return render(request, 'images_metadata/create_virtualobject.html', {'form': form})
    else:
        form = ImageThesaurusForm()
    return render(request, 'images_metadata/create_virtualobject.html', {'form': form})


@login_required
def update_file(request, pk):
    instance = get_object_or_404(ImageThesaurus, id=pk)
    if request.method == 'POST':
        form = ImageThesaurusForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('image_gallery:object_list')
        else:
            return render(request, 'images_metadata/create_virtualobject.html', {'form': form})
    else:
        form = ImageThesaurusForm(instance=instance)
    return render(request, 'images_metadata/create_virtualobject.html', {'form': form})
