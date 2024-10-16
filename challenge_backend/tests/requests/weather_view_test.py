import pytest
from challenge_backend.services.openweather.client import OpenWeatherClient
from challenge_backend.services.openweather.integration_error import IntegrationError


def test_successfully(mocker, client):
    mocker.patch.object(OpenWeatherClient, "get", return_value={"main": {"temp": 273}})

    response = client.get("/weather/?city=berlin")
    
    assert response.status_code == 200
    assert response.json()["data"]["kelvin"] == pytest.approx(273)
    assert response.json()["data"]["celcius"] == pytest.approx(-0.15)
    assert response.json()["data"]["farenheit"] == pytest.approx(32)



def test_fail_due_to_missing_param(client):

    response = client.get("/weather/")

    assert response.status_code == 400


def test_fail_due_to_integration_error(mocker, client):
    mocker.patch.object(OpenWeatherClient, "get", side_effect=IntegrationError())

    response = client.get("/weather/?city=campinas")

    assert response.status_code == 503

    assert response.json() == {"message": "Service Unavailable"}
