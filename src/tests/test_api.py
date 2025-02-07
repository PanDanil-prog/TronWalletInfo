import pytest

def test_get_wallet(client):

    response = client.post("api/wallet", json={"address": "TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ"})
    assert response.status_code == 200
    data = response.json()
    assert data["address"] == "TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ"
    assert "balance_trx" in data
    assert "energy" in data
    assert "bandwidth" in data

def test_get_wallet_requests(client):

    response = client.get("api/wallet-requests")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["items"], list)
