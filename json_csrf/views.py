from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json

# Create your views here.

@csrf_protect
def submit_feedback(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        comment = data.get('comment')

        response_data = {
            'message': f'Thank you {name} for your feedback!'
        }
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def show_page(request):
    return render(request, 'feedback.html')
