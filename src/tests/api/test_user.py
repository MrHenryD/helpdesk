def test_read_root(test_client):
    response = test_client.get("/user")
    assert response.status_code == 200
