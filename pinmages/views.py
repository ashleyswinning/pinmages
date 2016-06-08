from django.template.loader import get_template
from django.http import HttpResponse
from pinmages.models import Tag

def test(request):
    template = get_template('test.html')
    return HttpResponse(template.render())

def tags(request):
        allTags = Tag.objects.all()
	template = get_template('tags.html')
	return HttpResponse(template.render({'tags': allTags}))
