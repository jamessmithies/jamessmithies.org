from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.management import call_command
from index.models import Projects, Bio, Influences, Credits, Design, Publications

def index(request):
    return render(request, 'index/index.html',)

def projectsView(request):
    overview = Projects.objects.filter(title='Overview')
    projectdetails = Projects.objects.all().order_by('position').exclude(title='Overview')

    context = {'overview': overview, 'projectdetails': projectdetails,}
    
    return render(request, 'index/projects.html', context)

def bioView(request): 
    return render(request, 'index/bio.html', {
        'bio': get_object_or_404(Bio)
    })

def publicationsView(request):
    return render(request, 'index/publications.html', {
        'publications': get_object_or_404(Publications,)
    })

def designView(request):
    return render(request, 'index/design.html', {
        'design': get_object_or_404(Design,)
    })

def influencesView(request):
    return render(request, 'index/influences.html', {
        'influences': get_object_or_404(Influences,)
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






