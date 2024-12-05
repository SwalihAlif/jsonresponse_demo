from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
import json

# Create your views here.

@csrf_protect
def sweet_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        comment = data.get('comment')

        response_data = {
            'message': f'Thank you {name} for your Feedback!'
        }
        return JsonResponse(response_data)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


def sweet_page(request):
    return render(request, 'sweet_feedback.html')