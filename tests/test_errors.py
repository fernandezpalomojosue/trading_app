def test_404(client):
    response = client.get("/no-existe")
    assert response.status_code == 404
