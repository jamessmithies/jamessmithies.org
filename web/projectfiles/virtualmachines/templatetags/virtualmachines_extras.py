from virtualmachines.models import Tag, Type, Specification
from django import template
register = template.Library()


def virtualmachines_typelist():
    types = Type.objects.all()
    return {'types': types}

register.inclusion_tag('virtualmachines/types_all.html')(virtualmachines_typelist)

def virtualmachines_taglist():
    tags = Tag.objects.all()
    return {'tags': tags}

register.inclusion_tag('virtualmachines/tags_all.html')(virtualmachines_taglist)

def virtualmachines_latestlist():
    virtualmachines_latest = Specification.objects.all()
    return {'virtualmachines_latest': virtualmachines_latest}

register.inclusion_tag('virtualmachines/virtualmachines-latest_all.html')(virtualmachines_latestlist)





