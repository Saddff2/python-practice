from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data.decode() == "Hello from Daniel Tsoref"
        
def pytest_configure(config):
    config.addinivalue_line('markers', 'integration')
    

@pytest.ixture(scope='session')
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client