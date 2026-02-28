# Views handle requests and return responses

from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    info = f"METHOD: {request.method} | USER: {request.user} | INFO: {request}"
    print(info)

    # where the above variables come handy? in a case where one endpoint handles multiple requests

    if request.method == "POST":
        pass

    # processing - database, cache, rendering HTML template
    return HttpResponse("Hello, World. You're at polls index.")