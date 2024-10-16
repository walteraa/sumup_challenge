from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.renderers import JSONRenderer

from challenge_backend.services.openweather.integration_error import IntegrationError


class ErrorsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        try:
            response = self.get_response(request)
            if response.status_code == 404:
                response = Response({"message": "Not found"},
                                    status=status.HTTP_404_NOT_FOUND,
                                    content_type="application/json")
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
        except Exception:
            response = Response({"message": "Internal error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        return response
    

    def process_exception(self, _, e):
        if isinstance(e, ValidationError):
            response = Response({"errors": e.message_dict}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        elif isinstance(e, ObjectDoesNotExist):
            response = Response({"message": "Not found"},
                                status=status.HTTP_404_NOT_FOUND,
                                content_type="application/json")
        elif isinstance(e, IntegrationError):
            response = Response({"message": "Service Unavailable"},
                                status=status.HTTP_503_SERVICE_UNAVAILABLE,
                                content_type="application/json")

        else:
            response = Response({"message": "Internal error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        
        return response
        
