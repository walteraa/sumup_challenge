from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from challenge_backend.tasks.base_task import BaseTask



class HealthCheckView(APIView):
    

     def get(self, request):
         BaseTask().delay()
         return  Response({"status": "OK"}, status=status.HTTP_200_OK)



