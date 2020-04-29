from django.shortcuts import render
from django.http import HttpResponse

import json

def index(request):
    return HttpResponse(json.dumps({"msg": "index"}), content_type='application/json')


def house_prices(request):
    start_date = request.GET.get("from_date")
    end_date = request.GET.get("to_date")
    postcode = request.GET.get("postcode")
    
    
    return HttpResponse(json.dumps({"msg": "house_prices"}), content_type='application/json')


def transactions(request):
    return HttpResponse(json.dumps({"msg": "transactions"}), content_type='application/json')