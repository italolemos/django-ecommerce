from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


# def product_list(request):
#     context = {
#         'product_list': Product.objects.all()
#     }
#     return render(request, 'catalog/product_list.html', context)

class CategoryListView(ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

# def category(request, slug):
#     category = Category.objects.get(slug=slug)
#     context = {
#         'current_category': category,
#         'product_list': Product.objects.filter(category=category),
#     }
#     return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)