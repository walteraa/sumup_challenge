


from challenge_backend.services.openweather.client import OpenWeatherClient


class GetWeatherForCity:

    @staticmethod
    def call(city: str) -> dict:
        data = OpenWeatherClient().get(city) 

        temp = data.get("main", {}).get("temp")




        return {"kelvin": temp, "celcius": temp-273.15, "farenheit":  1.8*(temp-273) + 32}

