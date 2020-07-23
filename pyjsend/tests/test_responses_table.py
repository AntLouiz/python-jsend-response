import json
import mock
import re
import http
from .fixtures import table_responses, encoded_table_responses, response_table_object
from pyjsend.base import ResponsesTable


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data=encoded_table_responses)
def test_load_responses_table(mocked_file):
    file_path = 'some_table_response_file_path'

    with open(file_path, 'r') as file:
        response_table = file.read()
        response_table = json.loads(response_table)

    assert response_table == table_responses


def test_validate_response_table():
    data = table_responses
    keys = table_responses.keys()
    camel_case_regex = r'^[A-Z]+[a-z]+[A-Z]+\w+$'
    accepted_status = ['success', 'failure', 'error']
    accepted_http_codes = [status.value for status in list(http.HTTPStatus)]

    valid = True

    regex = re.compile(camel_case_regex)

    for key in keys:
        if not valid:
            break

        match_camel_case_regex = regex.match(key)

        http_code = data[key].get('http_code', False)
        status = data[key].get('status', False)

        if status not in accepted_status:
            valid = False
            break

        message = data[key].get('message', False)

        if status == accepted_status[0]:
            try:
                have_correct_data = bool(status and http_code)
                data[key]['data']

            except KeyError:
                have_correct_data = False
        else:
            have_correct_data = bool(status and message and http_code)

        have_correct_data = bool(have_correct_data and (http_code in accepted_http_codes))

        if not match_camel_case_regex or not have_correct_data:
            valid = False

    assert True if valid else False


def test_responses_table_instance_file_path(response_table_object):
    assert response_table_object.file == response_table_file_path


def test_response_table_availabe_codes(response_table_object):
    assert response_table_object.codes == table_responses
