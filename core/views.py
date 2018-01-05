from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView


from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'index.html'

#
# def index(request):
#     return render(request, 'index.html')


def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

