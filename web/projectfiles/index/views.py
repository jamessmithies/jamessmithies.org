from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.core.management import call_command
from .models import Projects, Bio, Credits, Design, Research

def index(request):
    return render(request, 'index/index.html',)

def projectsView(request):
    overview = Projects.objects.filter(title='Overview')
    projectdetails = Projects.objects.all().order_by('position').exclude(title='Overview')

    context = {'overview': overview, 'projectdetails': projectdetails,}
    
    return render(request, 'index/projects.html', context)

def researchView(request):
    research = Research.objects.filter(title='Research')
    researchdetails = Research.objects.all().order_by('id').exclude(title='Research')
    
    context = {'research': research, 'researchdetails': researchdetails,}

    return render(request, 'index/research.html', context)

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

def mastodonsidebarView(request):
    return render(request, 'index/mastodon_sidebar.html',)

def updatezoteroView(request):
    call_command('zotcommand')
    return render(request, 'zotero/update-zotero.html')

def updatemastodonView(request):
    call_command('mastocommand')
    return render(request, 'index/update-mastodon.html')



