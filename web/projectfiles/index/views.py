from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.management import call_command
from .models import Projects, Bio, Credits, Design, Writing, Talks

def index(request):
    return render(request, 'index/index.html',)

def projectsView(request):
    overview = Projects.objects.filter(title='Overview')
    projectdetails = Projects.objects.all().order_by('position').exclude(title='Overview')

    context = {'overview': overview, 'projectdetails': projectdetails,}
    
    return render(request, 'index/projects.html', context)

def writingView(request):
    writing = Writing.objects.filter(title='Writing')
    writingdetails = Writing.objects.all().order_by('position').exclude(title='Writing')
    
    context = {'writing': writing, 'writingdetails': writingdetails,}

    return render(request, 'index/writing.html', context)

def talksView(request):
    talks = Talks.objects.filter(title='Talks')
    talksdetails = Talks.objects.all().order_by('position').exclude(title='Talks')
    
    context = {'talks': talks, 'talksdetails': talksdetails,}

    return render(request, 'index/talks.html', context)

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

def updatezoterowritingView(request):
    call_command('updatezoterowriting')
    return render(request, 'zotero/update-zotero.html')

def updatezoterotalksView(request):
    call_command('updatezoterotalks')
    return render(request, 'zotero/update-zotero.html')




