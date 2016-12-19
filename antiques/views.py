from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Category, Type


class IndexView(generic.ListView):
    template_name = 'antiques/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


class CategoryIndexView(generic.ListView):
    template_name = 'antiques/category_index.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryIndexView, self).get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['category'] = get_object_or_404(Category, pk=self.kwargs['category_id'])
        return context


class TypeDetail(generic.DetailView):
    template_name = 'antiques/type.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(TypeDetail, self).get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['type'] = get_object_or_404(Type, pk=self.kwargs['type_id'])
        return context


