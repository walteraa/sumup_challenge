from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from challenge_backend.use_cases.get_weather_for_city import GetWeatherForCity

class WeatherView(APIView):

    def get(self, request):
        city = request.query_params.get("city")

        if city is None:
            return Response({"error": "City is missing"}, 400)

        data = GetWeatherForCity.call(city)


        return Response({"data": data}, 200)

