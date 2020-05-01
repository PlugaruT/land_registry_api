import json
from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from .queries import get_average_price, group_transaction_prices

DATE_FORMAT = "%Y-%m-%d"


def is_valid_date_str(date_str):
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

    if (start_date and not is_valid_date_str(start_date)) or (
        end_date and not is_valid_date_str(end_date)
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
    a_year_ago = datetime.now() - timedelta(days=365)
    start_date = request.GET.get("from_date", a_year_ago.strftime(DATE_FORMAT))
    end_date = request.GET.get("to_date")
    postcode = request.GET.get("postcode")

    if (start_date and not is_valid_date_str(start_date)) or (
        end_date and not is_valid_date_str(end_date)
    ):
        return HttpResponseBadRequest(
            json.dumps({"error": "Invalid date format. Should be YYYY-MM-DD"}),
            content_type="application/json",
        )

    data = group_transaction_prices(
        start_date=start_date, end_date=end_date, postcode=postcode
    )

    response = {}
    for item in data:
        response[item["range"]] = item["cnt"]

    return HttpResponse(json.dumps({"data": response}), content_type="application/json")
