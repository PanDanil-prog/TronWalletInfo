import pytest

@pytest.mark.asyncio
def test_get_wallet(client):

    response = client.post("api/wallet", json={"address": "TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ"})
    assert response.status_code == 200
    data = response.json()
    assert data["address"] == "TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ"
    assert "balance_trx" in data
    assert "energy" in data
    assert "bandwidth" in data
