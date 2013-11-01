#!/usr/bin/python

from django.http import Http404, HttpResponse
import datetime

def hello(request):
    """docstring for hello"""
    return HttpResponse("Hello world!") 

def current_datetime(request):
    """docstring for current_datetime"""
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    """docstring for hours_ahead"""
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

