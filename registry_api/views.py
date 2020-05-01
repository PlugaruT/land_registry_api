import json
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from .queries import get_average_price

DATE_FORMAT = "%Y-%m-%d"


def validate_date_param(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        return False
    return True


def index(request):
    return HttpResponse(json.dumps({"msg": "index"}), content_type="application/json")


def house_prices(request):
    start_date = request.GET.get("from_date")
    end_date = request.GET.get("to_date")
    postcode = request.GET.get("postcode")

    if (start_date and not validate_date_param(start_date)) or (
        end_date and not validate_date_param(end_date)
    ):
        return HttpResponseBadRequest(
            json.dumps({"error": "Invalid date format. Should be YYYY-MM-DD"}),
            content_type="application/json",
        )

    data = get_average_price(
        start_date=start_date, end_date=end_date, postcode=postcode
    )

    response = {}

    for item in data:
        response[item["period"].strftime(DATE_FORMAT)] = {
            "average_price": float(item["average_price"]),
            "property_type": item["property_type"],
        }

    return HttpResponse(json.dumps({"data": response}), content_type="application/json")


def transactions(request):
    start_date = request.GET.get("from_date")
    end_date = request.GET.get("to_date")
    postcode = request.GET.get("postcode")

    if (start_date and not validate_date_param(start_date)) or (
        end_date and not validate_date_param(end_date)
    ):
        return HttpResponseBadRequest(
            json.dumps({"error": "Invalid date format. Should be YYYY-MM-DD"}),
            content_type="application/json",
        )

    return HttpResponse(
        json.dumps({"data": "transactions"}), content_type="application/json"
    )
