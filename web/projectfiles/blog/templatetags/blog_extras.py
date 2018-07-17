from blog.models import Tag, Category, Blogroll, Entry
from django import template
register = template.Library()



def blog_categorylist():
    categories = Category.objects.all()
    return {'categories': categories}

register.inclusion_tag('blog/categories_all.html')(blog_categorylist)

def blog_categorylist_pipes():
    categories = Category.objects.all()
    return {'categories': categories}

register.inclusion_tag('blog/categories_all_pipes.html')(blog_categorylist_pipes)

def blog_taglist():
    tags = Tag.objects.all()
    return {'tags': tags}

register.inclusion_tag('blog/tags_all.html')(blog_taglist)

def blog_taglist_pipes():
    tags = Tag.objects.all()
    return {'tags': tags}

register.inclusion_tag('blog/tags_all_pipes.html')(blog_taglist_pipes)

def blog_two_recent():
    two_recent = Entry.objects.all()[:2]
    return {'two_recent': two_recent}

register.inclusion_tag('blog/blog_two_recent.html')(blog_two_recent)

def blog_blogroll():
    blogroll = Blogroll.objects.all()
    return {'blogroll': blogroll}

register.inclusion_tag('blog/blogroll.html')(blog_blogroll)





