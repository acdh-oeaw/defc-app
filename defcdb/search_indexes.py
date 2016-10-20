from haystack import indexes
from .models import Area, Finds


class AreaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Area

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(public=True)


class FindsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Finds

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(public=True)
