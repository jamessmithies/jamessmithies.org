from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Entry, Category, Tag, Blogroll

import datetime, time

def blogindexView(request, selected_page=1):
	context_object_name = 'home_list'
	entries = Entry.objects.all().order_by('-pub_date')
	tags = Tag.objects.all()
	categories = Category.objects.all()
	pages = Paginator(entries, 2)
	returned_page = pages.page(selected_page) 

	context = {'entries':returned_page.object_list,'page':returned_page, 'tags':tags, 'categories': categories,}

	try:
		returned_page = pages.page(selected_page)

	except EmptyPage:
		returned_page = pages.page(pages.num_pages)

	return render(request, 'blog/home.html', context)

class entrydetailView(DetailView):
	model = Entry
	template_name = 'blog/entry_detail.html'

def categorylistView(request, slug, selected_page=1):
	context_object_name = 'category_list'
	categories = get_object_or_404(Category, slug=slug)
	entries = Entry.objects.filter(categories=categories)
	pages = Paginator(entries, 2)
	returned_page = pages.page(selected_page)

	context = {'entries':returned_page.object_list,'page':returned_page,'categories': categories,}

	try:
		returned_page = pages.page(selected_page)

	except EmptyPage:
		returned_page = pages.page(pages.num_pages)

	return render(request, 'blog/category_list.html', context)

class taglistView(DetailView):
	model = Tag
	template_name = 'blog/tag_list.html'

def tagsView(request):
	return render(request, 'blog/tags.html', { 'tags': Tag.objects.all()})

def categoriesView(request):
	return render(request, 'blog/categories.html', { 'categories': Category.objects.all()})

def blogrollView(request):
	return render(request, 'blog/blogroll.html', { 'blogroll': Blogroll.objects.all()})

# Bespoke view used instead of DetailView, in conjunction with redirect, to handle legacy Wordpress urls.
def entryView(request, year, month, day, slug):
    """Returns an individual entry."""
    date = datetime.date(int(year), int(month), int(day))
    entry = Entry.objects.get(slug=slug, pub_date__year=date.year,
                            pub_date__month=date.month, pub_date__day=date.day)

    context = {'entry': entry}
 
    return render(request, 'blog/entry_detail.html', context)
