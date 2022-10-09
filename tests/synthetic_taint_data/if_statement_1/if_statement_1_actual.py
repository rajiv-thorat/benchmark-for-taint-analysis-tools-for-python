#!/usr/bin/env python3
from django.http import HttpRequest, HttpResponse

def if_route(request: HttpRequest) -> HttpResponse:
    operator = request.GET["operator"]
    i = 10
    if i > 0:
        # This sink will always be reached
        result = eval(f"2 {operator} 2")
        return result
