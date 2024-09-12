from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Student_create(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            
            # Pass parsed data to the serializer
            serializer = StudentSerializer(data=pythondata)
            
            # Check if the data is valid
            if serializer.is_valid():
                serializer.save()  # Save the valid data
                res = {'msg': 'Data Created'}
                
                # Render the response as JSON
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            else:
                # If the data is not valid, return errors
                json_data = JSONRenderer().render(serializer.errors)
                return HttpResponse(json_data, content_type='application/json')
        except Exception as e:
            # Handle any parsing or other errors
            return HttpResponse(
                content=json.dumps({'error': str(e)}),
                content_type='application/json',
                status=400
            )
    else:
        return HttpResponse(
            content=json.dumps({'error': 'Only POST method is allowed'}),
            content_type='application/json',
            status=405
        )
