from django.template.loader import get_template
from django.http import HttpResponse
from pinmages.models import Tag
from random import choice

def getsampletags():
    allTags = [{'name': 'thisisthelongestatagwilleverbe'}, {'name': 'bar'}, {'name': 'anothertag'}]
    colors = ["#93B5C6", "#D3F954", "#F0CF65", "#D7816A", "#BD4F6C"]
    tagsWithColors = [ {'name': tag.get('name'), 'color': choice(colors)} for tag in allTags]
    return tagsWithColors

def test(request):
    template = get_template('test.html')
    return HttpResponse(template.render())

def tags(request):
    template = get_template('tags.html')
    return HttpResponse(template.render({'tags': getsampletags()}))

def search(request):
    template = get_template('headerbar.html')
    return HttpResponse(template.render())

def tagsdescription(request):
    template = get_template('tagsdescription.html')
    return HttpResponse(template.render({'tags': [], 'description': 'Here is a description'}))

def image(request):
    template = get_template('image.html')
    return HttpResponse(template.render({'svg_data': 'Here is the photo'}))

def getgriddata():
    grid_data = [{'svg_data': "this is an image", 'name': "heart"}]
    return grid_data

def grid(request):
    template = get_template('grid.html')
    return HttpResponse(template.render({'grid_data': getgriddata()}))

def gridedit(request):
    template = get_template('gridedit.html')
    image = [{'svg_data': "this is an image"}]
    return HttpResponse(template.render({'grid_data': image}))

def viewgrid(request):
    template = get_template('viewgrid.html')
    return HttpResponse(template.render({'tags':getsampletags(), 'grid_data':getgriddata()}))



