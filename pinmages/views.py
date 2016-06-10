from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from forms import UploadFileForm
from pinmages.models import Tag
from pinmages.models import Image
from random import choice
from image_logic import get_png_bytestring
import django
#TODO re-enable csrf
from django.views.decorators.csrf import csrf_exempt

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
    grid_data = [{'svg_data': "this is an image", 'name': "heart"}, {'svg_data': "this is an image", 'name': "star"}, {'svg_data': "this is an image", 'name': "smile"}, {'svg_data': "this is an image", 'name': "sparkle"}, {'svg_data': "this is an image", 'name': "unicorn"}, {'svg_data': "this is an image", 'name': "glittery"}]
    return grid_data

def grid(request):
    template = get_template('grid.html')
    return HttpResponse(template.render({'grid_data': getgriddata()}))

def gridedit(request):
    template = get_template('gridedit.html')
    image = [{'svg_data': "this is an image"}]
    return HttpResponse(template.render({'grid_data': image}))

def viewgrid(request):
    images = Image.objects.all()
    print images
    template = get_template('viewgrid.html')
    return HttpResponse(template.render({'tags':getsampletags(), 'grid_data':images}))


def imageinformation(request):
    template = get_template('imageinfo.html')
    return HttpResponse(template.render())
   
    
def imageedit(request):
	template = get_template('imageedit.html')
	return HttpResponse(template.render({'tags':getsampletags(), 'image_data': {'svg_data': 'image goes here', 'description':'the description', 'name': 'image name', 'owner': 'the owner', 'tags':getsampletags()}}))

def download_image(request, id):
    svg_data = open('./pinmages/red_heart.svg').read()
    width = request.GET.get('width')
    height = request.GET.get('height')
    width = int(width) if width is not None and height.isdigit() else None
    height = int(height) if height is not None and height.isdigit() else None
    bs = get_png_bytestring(svg_data, width, height)
    res = HttpResponse(bs, content_type='application/force-download')
    res['Content-Disposition'] = 'attachment; filename=my_sprite.png'
    return res
    

def handle_uploaded_file(f):
    bytestring = f.read()
    i = Image(svg_data=bytestring, name="test_image", description="hi")
    i.save()
    print bytestring

@csrf_exempt
def imageupload(request):
        if request.method == 'POST':
            handle_uploaded_file(request.FILES['files[]'])
	template = get_template('imageupload.html')
	return HttpResponse(template.render())
