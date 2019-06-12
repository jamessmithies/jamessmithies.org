from django.db import models 
from ckeditor.fields import RichTextField
from django.urls import reverse

class Home(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128)
    about = RichTextField(blank=True,)

    class Meta:
        verbose_name_plural = "Home"
        app_label = 'virtualmachines'  

    def __unicode__(self):
        return self.title

class Help(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    content = RichTextField(blank=True,)

    def get_absolute_url(self):
        return "/sandpit/%s/" % self.slug 

    class Meta:
        verbose_name_plural = "Help Topics"
        app_label = 'virtualmachines'  

    def __unicode__(self):
        return self.slug

class Type(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True, max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    description = RichTextField(blank=True,)

    def get_absolute_url(self):
        return "/virtualmachines/types/%s/" % self.slug 

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Types"
        app_label = 'virtualmachines'

    def __unicode__(self):
        return self.title

class Tag (models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(blank=True, max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    description = RichTextField(blank=True,)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Tags"
        app_label = 'virtualmachines' 

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/virtualmachines/tags/%s/" % self.slug 


class Specification(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    type = models.ForeignKey(Type, on_delete = models.CASCADE)
    product1 = models.CharField("Product1 Name", max_length=128, blank=True)
    website1 = models.URLField("Website1", blank=True)
    about1 = RichTextField("About1", blank=True)
    product2 = models.CharField("Product2 Name", max_length=128, blank=True)
    website2 = models.URLField("Website2", blank=True)
    about2 = RichTextField("About2", blank=True)
    name = models.TextField("AMI Name", blank=True)
    description = models.TextField("AMI Description", blank=True)
    file_size = models.TextField("File Size", blank=True)
    ami_id = models.TextField("ID", blank=True)
    os = models.TextField("Operating System", blank=True)
    app_installs = models.TextField("Applications Installed", blank=True)
    server = models.TextField("Server", blank=True)
    server_additions = models.TextField("Server Additions", blank=True)
    plugins = models.TextField("Plugins", blank=True)
    version = models.CharField(max_length=128, blank=True)
    last_modified = models.DateTimeField("Last Modified", blank=True)
    last_tested = models.DateTimeField("Last Tested", blank=True)
    views = models.IntegerField(null=True, default=0, unique=False)
    user_tests = models.IntegerField(null=True, default=0)
    notes = RichTextField("Notes", blank=True)
    readMe= models.URLField("ReadMe", blank=True)
    launch = models.URLField("Launch URL", blank=True)
    download = models.URLField("Download URL", blank=True)
    quick_download = models.BooleanField("Quick Download from homepage?", default=False)
    quick_launch = models.BooleanField("Quick Launch from homepage?", default=False)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return "/virtualmachines/%s/" % self.slug 
  
    class Meta:
        verbose_name_plural = "Specifications"
        app_label = 'virtualmachines'  

    def __unicode__(self):
        return self.title

