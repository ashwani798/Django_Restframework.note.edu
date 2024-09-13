from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt here

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.query_params.get('id', None)
        
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Created'}, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')

        try:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=pythondata, partial=True)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'Data Updated'}, status=200)
            return JsonResponse(serializer.errors, status=400)

        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    
    elif request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')

        try:
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg': 'Data Deleted!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
