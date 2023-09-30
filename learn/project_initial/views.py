from django.http import HttpResponse
from django.template import loader

def user(request):
    template = loader.get_template('initial.html')
    return HttpResponse(template.render())