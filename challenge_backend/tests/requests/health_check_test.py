

def test_success(client):
    req = client.get("/health/")

    assert req.status_code == 200
