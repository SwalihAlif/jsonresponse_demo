from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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

#----------- JsonResponse GET and POST  -----------------------------------------------------------------------------------

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def show_json_form(request):
    return render(request, 'json_form.html')

@csrf_exempt  # Only for development. Ensure CSRF protection in production.
def my_json_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')

        response_data = {
            'message': f'Hello {name}, you are {age} years old!'
        }
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)




