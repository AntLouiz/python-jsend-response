import json
import mock
import re
import http
from .fixtures import table_responses, encoded_table_responses, response_table_object
from pyjsend.settings import RESPONSES_TABLE_FILE_PATH



def test_validate_response_table(table_responses):
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
    assert response_table_object.file == RESPONSES_TABLE_FILE_PATH


def test_response_table_availabe_codes(response_table_object, table_responses):
    assert response_table_object.codes == table_responses
