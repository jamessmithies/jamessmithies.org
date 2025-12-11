from django.db import models 
from ckeditor.fields import RichTextField  
from ckeditor_uploader.fields import RichTextUploadingField

class Projects(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    position = models.IntegerField(default=0,)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    about = RichTextField("About", blank=True)

    class Meta:
        verbose_name_plural = "Projects"
        app_label = 'index'  
    
    def __str__(self):
        return self.title

class Bio(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    about = RichTextUploadingField("About", blank=True)
    
    class Meta:
        verbose_name_plural = "Bio"
        app_label = 'index'  
    
    def __str__(self):
        return self.title

class Design(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    about = RichTextUploadingField("About", blank=True)
    
    class Meta:
        verbose_name_plural = "Site Design"
        app_label = 'index'  
    
    def __str__(self):
        return self.title

class Credits(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    about = RichTextUploadingField("About", blank=True)
    
    class Meta:
        verbose_name_plural = "Site Credits"
        app_label = 'index'  
    
    def __str__(self):
        return self.title

class Research(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", help_text='Suggested value automatically generated from title. Must be unique.')
    about = RichTextUploadingField("About", blank=True)
    
    class Meta:
        verbose_name_plural = "Research"
        app_label = 'index'  
    
    def __str__(self):
        return self.title



