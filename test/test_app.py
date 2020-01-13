# Using py.test framework
from service import Iris, Intro


def test_example_message(client):
    """Example message should be returned"""
    client.app.add_route('/iris', Intro())

    result = client.simulate_get('/iris')
    assert result.json == {
        'message': 'This service verifies a model using the Iris Test data set. '
                   'Invoke using the form /Iris/<index of test sample>. For example, /iris/24'}


def test_classification_request(client):
    """Classification for Iris sample should be returned"""
    client.app.add_route('/iris/{index:int(min=0)}', Iris())

    result = client.simulate_get('/iris/1')
    assert result.json == {"index": 1, "predicted_label": "setosa", "predicted": 0}
