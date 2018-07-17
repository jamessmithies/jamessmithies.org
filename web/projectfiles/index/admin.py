from django.contrib import admin
from django.db import models
from index.models import Projects, Bio, Influences, Design, Credits, Publications


class InfluencesAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Influences, InfluencesAdmin)

class DesignAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Design, DesignAdmin)

class CreditsAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Credits, CreditsAdmin)

class PublicationsAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Publications, PublicationsAdmin)

class BioAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Bio, BioAdmin)

class ProjectsAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce',
            '/static/tinymce_setup.js',)

admin.site.register(Projects, ProjectsAdmin)


