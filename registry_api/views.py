from django.shortcuts import render
from django.http import HttpResponse

import json

def index(request):
    return HttpResponse(json.dumps({"msg": "index"}), content_type='application/json')


def house_prices(request):
    return HttpResponse(json.dumps({"msg": "house_prices"}), content_type='application/json')


def transactions(request):
    return HttpResponse(json.dumps({"msg": "transactions"}), content_type='application/json')