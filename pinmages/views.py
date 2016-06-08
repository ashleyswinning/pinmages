from django.template.loader import get_template
from django.http import HttpResponse
from pinmages.models import Tag
from random import choice

def test(request):
    template = get_template('test.html')
    return HttpResponse(template.render())

def tags(request):
    allTags = [{'name': 'foo'}, {'name': 'bar'}]
    colors = ["#93B5C6", "#E0F98E", "#F0CF65", "#D7816A", "#BD4F6C"]
    tagsWithColors = [ {'name': tag.get('name'), 'color': choice(colors)} for tag in allTags]
    template = get_template('tags.html')
    return HttpResponse(template.render({'tags': tagsWithColors}))

def search(request):
    template = get_template('headerbar.html')
    return HttpResponse(template.render())
