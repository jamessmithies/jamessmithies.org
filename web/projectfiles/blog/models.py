import datetime
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Blogroll (models.Model):
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	url = models.URLField()

	class Meta:
		ordering = ['title']
		verbose_name_plural = "Blogroll"
		app_label = 'blog' 

	def __unicode__(self):
		return self.title

class Category (models.Model):
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	slug = models.SlugField(unique=True, help_text='Suggested value automatically generated from title. Must be unique.')
	description = models.TextField()

	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"
		app_label = 'blog' 

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/blog/categories/%s/" % self.slug 

class Tag (models.Model):
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	slug = models.SlugField(unique=True, help_text='Suggested value automatically generated from title. Must be unique.')
	description = models.TextField()

	class Meta:
		ordering = ['title']
		verbose_name_plural = "Tags"
		app_label = 'blog' 

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/blog/tags/%s/" % self.slug 


class Entry(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
		(LIVE_STATUS, 'Live'),
		(DRAFT_STATUS, 'Draft'),
		(HIDDEN_STATUS, 'Hidden'),
		)
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
	hero_image = models.ImageField(upload_to='uploads/', null=True, blank=True, help_text='Required size = 1440 x 378.')
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	excerpt = RichTextUploadingField(blank=True, help_text='A short summary of the entry. Optional.')
	body = RichTextUploadingField(blank=True,)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	slug = models.SlugField(max_length=250, unique_for_date='pub_date', help_text='Suggested value automatically generated from title.')
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)

	class Meta:
		verbose_name_plural = "Entries"
		ordering = ['-pub_date']
		app_label = "blog"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/blog/%s/%s/" % (self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)
