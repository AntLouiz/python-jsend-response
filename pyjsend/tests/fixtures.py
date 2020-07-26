import json
import pytest
import yaml
from pyjsend.base import ResponsesTable, Response
from pyjsend.settings import RESPONSES_TABLE_FILE_PATH


@pytest.fixture
def table_responses():
    file = open(RESPONSES_TABLE_FILE_PATH, 'r')
    response = yaml.load(file.read(), Loader=yaml.FullLoader)
    file.close()

    return response


@pytest.fixture
def encoded_table_responses():
    file = open(RESPONSES_TABLE_FILE_PATH, 'r')
    response = yaml.load(file.read(), Loader=yaml.FullLoader)
    file.close()

    return json.dumps(response)


@pytest.fixture
# @mock.patch("builtins.open", new_callable=mock.mock_open, read_data=encoded_table_responses)
def response_table_object():
    response_table = ResponsesTable(RESPONSES_TABLE_FILE_PATH)

    return response_table


@pytest.fixture
def response_object():
    response = Response('BadRequest')

    return response
