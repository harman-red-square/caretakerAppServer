from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from settings.models import settings
from settings.serializers import settingserializer
from settings.NetworkConnectivity.models import Network
from settings.NetworkConnectivity.serializers import NetworkSerializer


# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def geo_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        network = Network.objects.all()
        serializer = NetworkSerializer(network, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NetworkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

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
        setting = settings.objects.all()
        serializer = settingserializer(setting, many=True)
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
        setting = settings.objects.get(pk=pk)
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