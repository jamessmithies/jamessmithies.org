from django.contrib import admin
from django.db import models
from blog.models import Category, Entry, Tag

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Entry, EntryAdmin)

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Tag, TagAdmin)