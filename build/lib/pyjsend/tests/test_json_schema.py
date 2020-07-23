
import pytest
import json
from pyjsend.base import Response, ResponsesTable
from pyjsend.tests.fixtures import response_object, response_table_object
from pyjsend.exceptions import MissingResponseCode


def test_json_schema_table_of_responses_composition(response_object):
    assert isinstance(response_object._responses_table, ResponsesTable)


def test_json_schema_invalid_input():

    response = Response('InvalidValueType')

    assert response.http_code == 400
    assert response.message == 'The value specified is invalid.'


def test_json_schema_success_code():
    email = 'some@email.com'

    response = Response('SuccessfullLogin', data={'email': email})

    assert response.http_code == 200


def test_json_schema_to_json_method():
    email = 'some@email.com'

    response = Response('SuccessfullLogin', data={'email': email})

    assert response.to_json()


def test_json_schema_missing_response_code():

    with pytest.raises(MissingResponseCode) as e:
        response = Response('SomemissingResponseCode')

    assert str(e.value) == 'Missing response code in table of responses.'