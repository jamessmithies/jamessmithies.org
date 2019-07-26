from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.management import call_command
from .models import Projects, Bio, Credits, Design, Outputs

def index(request):
    return render(request, 'index/index.html',)

def projectsView(request):
    overview = Projects.objects.filter(title='Overview')
    projectdetails = Projects.objects.all().order_by('position').exclude(title='Overview')

    context = {'overview': overview, 'projectdetails': projectdetails,}
    
    return render(request, 'index/projects.html', context)

def outputsView(request):
    outputs = Outputs.objects.filter(title='Outputs')
    outputdetails = Outputs.objects.all().order_by('position').exclude(title='Outputs')

    context = {'outputs': outputs, 'outputdetails': outputdetails,}

    return render(request, 'index/outputs.html', context)

def bioView(request): 
    return render(request, 'index/bio.html', {
        'bio': get_object_or_404(Bio)
    })

def designView(request):
    return render(request, 'index/design.html', {
        'design': get_object_or_404(Design,)
    })

def creditsView(request):
    return render(request, 'index/credits.html', {
        'credits': get_object_or_404(Credits,)
    })

def architectureView(request, slug): 
    return render(request, 'index/architecture.html', {
        'architecture': get_object_or_404(Architecture, slug=slug)
    })

def updatezoteroView(request):
    call_command('updatezotero')
    return render(request, 'zotero/update-zotero.html')






