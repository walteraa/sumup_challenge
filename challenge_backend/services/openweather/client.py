import requests
from django.conf import settings

from challenge_backend.services.openweather.integration_error import IntegrationError


class OpenWeatherClient:

    BASE_URL = settings.OPENWEATHER.get("BASE_URL")
    API_KEY = settings.OPENWEATHER.get("API_KEY")

    def get(self, city) -> dict:
        req = requests.get(f"{self.BASE_URL}/weather?q={city}&appid={self.API_KEY}")
        
        if req.status_code != 200:
            raise IntegrationError()

        return req.json()
        
