from django.http import HttpRequest, HttpResponse
from subprocess import check_call


def operate_on_twos(request: HttpRequest) -> HttpResponse:
    operator = request.GET["operator"]

    result = eval(f"2 {operator} 2")  # noqa: P204

    result2 = check_call([operator])

    return result