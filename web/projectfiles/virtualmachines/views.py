from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView, View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .forms import specificationPageSearchForm
from .models import Home, Specification, Help, Tag, Type


def homepageView(request):
    about = Home.objects.get().about
    last_modified = Specification.objects.all().order_by('last_modified')
    quick_download = Specification.objects.filter(quick_download=True)
    quick_launch = Specification.objects.filter(quick_launch=True)

    context = {'quick_launch':quick_launch,'last_modified':last_modified, 'about': about, 'quick_download': quick_download,}
    
    return render(request, 'virtualmachines/home.html', context)


def SpecificationView(request, slug):   
    return render(request, 'virtualmachines/specification.html', {
        'specification': get_object_or_404(Specification, slug=slug)
    })

def HelpView(request, slug): 
    return render(request, 'virtualmachines/help.html', {
        'help': get_object_or_404(Help, slug=slug)
    })

class virtualmachines_typelistView(DetailView):
    model = Type
    template_name = 'virtualmachines/type_list.html'

def virtualmachines_typesView(request):
    return render(request, 'virtualmachines/types.html', { 'Types': Type.objects.all()})

class virtualmachines_taglistView(DetailView):
    model = Tag
    template_name = 'virtualmachines/tag_list.html'

def virtualmachines_tagsView(request):
    return render(request, 'virtualmachines/tags.html', { 'tags': Tag.objects.all()})

def latestView(DetailView):
    return render(request, 'virtualmachines/virtualmachines-latest_all.html', { 'Latest': Specification.objects.all().order_by('last_modified')})




