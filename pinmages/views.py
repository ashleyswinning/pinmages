from django.template.loader import get_template
from django.http import HttpResponse

def test(request):
    template = get_template('test.html')
    return HttpResponse(template.render())

def tags(request):
	template = get_template('tags.html')
	return HttpResponse(template.render())
