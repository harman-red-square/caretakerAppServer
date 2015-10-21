from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from settings.models import setting
from settings.serializers import settingserializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def settings_list(request):
    """
    List all code settings, or create a new settings.
    """
    if request.method == 'GET':
        settings = setting.objects.all()
        serializer = settingserializer(settings, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = settingserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def settings_detail(request, pk):
    """
    Retrieve, update or delete a code settings.
    """
    try:
        settings = setting.objects.get(pk=pk)
    except settings.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = settingserializer(settings)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = settingserializer(settings, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        settings.delete()
        return HttpResponse(status=204)
from django.shortcuts import render

# Create your views here.
