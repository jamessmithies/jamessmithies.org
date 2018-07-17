from django.contrib import admin
from django.db import models
from virtualmachines.models import Home, Specification, Help, Type, Tag

admin.site.register(Home)



class HelpAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Help, HelpAdmin)


class SpecificationAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Specification, SpecificationAdmin)

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Tag, TagAdmin)

class TypeAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Type, TypeAdmin)