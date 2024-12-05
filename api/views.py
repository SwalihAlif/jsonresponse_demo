from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

#----------- example of simple JsonResponse -----------------------------------------------------------------------------------

def sample_json_response(request):
    data = {
        "message": "Hello, JsonResponse!",
        "status": "Success",
        "data": {
            "id": 1,
            "name": "Muhammed Swalih M",
            "place": "Pookkottur"
        }
    }
    return JsonResponse(data)

#----------- example of simple JsonResponse -----------------------------------------------------------------------------------
