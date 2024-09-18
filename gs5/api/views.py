from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentAPI(APIView):

    def get(self, request, *args, **kwargs):
        id = request.GET.get('id', None)
        
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        
        try:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data Updated!'}, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Student.DoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        
        try:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({'msg': 'Data Deleted!'}, status=status.HTTP_204_NO_CONTENT)
        
        except Student.DoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
