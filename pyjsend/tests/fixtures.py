import json
import pytest
import mock
from pyjsend.base import ResponsesTable


table_responses = {
        'InvalidValueType': {
            'http_code': 400,
            'status': 'failure',
            'message': 'The value specified is invalid.',
        },
        'SuccessfullLogin': {
            'http_code': 200,
            'status': 'success',
            'data': {}
        },
        'EntityAlreadyExists': {
            'http_code': 409,
            'status': 'failure',
            'message': 'The specified entity already exists.'
        },
        'NotImplemented': {
            'http_code': 501,
            'status': 'error',
            'message': 'The requested operation is not implemented on the specified resource.'
        }
}

encoded_table_responses = json.dumps(table_responses)


@pytest.fixture
@mock.patch("builtins.open", new_callable=mock.mock_open, read_data=encoded_table_responses)
def response_table_object(mocked_file):
    response_table = ResponsesTable('somefilepath')

    return response_table
