
def test_json_schema_table_of_responses_composition():
    response = JSResponse('SuccessfullLogin')

    assert isinstance(response._responses_table, ResponsesTable)


def test_json_schema_invalid_input():

    response = JSResponse('InvalidValueType')

    assert response.http_code == 400
    assert response == {
        'status': 'failure',
        'http_code': 'InvalidValueType',
        'data': {
            'message': 'The value specified is invalid.'
        }
    }


def test_json_schema_success_code():
    email = 'some@email.com'

    response = JSResponse('SuccessfullLogin', data={'email': email})

    assert response.http_code == 200
    assert response == {
        'status': 'sucess',
        'http_code': 'SuccessfullLogin',
        'data': {
            'message': "User logged in successfully"
        }
    }


def test_json_schema_to_json_method():
    email = 'some@email.com'

    response = JSResponse('SuccessfullLogin', data={'email': email})

    assert response.to_json() == json.dumps(response)


def test_json_schema_missing_response_code():

    with pytest.raises(MissingResponseCode) as e:
        response = JSResponse('SomemissingResponseCode')

    assert str(e.value) == 'Missing response code in table of responses.'
