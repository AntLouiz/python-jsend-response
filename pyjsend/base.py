import json
import re
import http
from pyjsend.settings import RESPONSES_TABLE_FILE_PATH
from pyjsend.exceptions import MissingResponseCode


class ResponsesTable:
    def __init__(self, file_path):
        self.file = file_path
        self.codes = None
        self._load_responses_table()

    def _load_responses_table(self):
        with open(self.file, 'r') as file:
            response_table = file.read()
            response_table = json.loads(response_table)

            valid_codes = self.validate(response_table)

            if valid_codes:
                self.codes = response_table

    def validate(self, codes):
        keys = codes.keys()
        camel_case_regex = r'^[A-Z]+[a-z]+[A-Z]+\w+$'
        accepted_status = ['success', 'failure', 'error']
        accepted_http_codes = [status.value for status in list(http.HTTPStatus)]

        valid = True

        regex = re.compile(camel_case_regex)

        for key in keys:
            if not valid:
                break

            match_camel_case_regex = regex.match(key)

            http_code = codes[key].get('http_code', False)
            status = codes[key].get('status', False)

            if status not in accepted_status:
                valid = False
                break

            message = codes[key].get('message', False)

            if status == accepted_status[0]:
                try:
                    have_correct_data = bool(status and http_code)
                    codes[key]['data']

                except KeyError:
                    have_correct_data = False
            else:
                have_correct_data = bool(status and message and http_code)

            have_correct_data = bool(have_correct_data and (http_code in accepted_http_codes))

            if not match_camel_case_regex or not have_correct_data:
                valid = False

            return valid


class Response:
    _responses_table = ResponsesTable(RESPONSES_TABLE_FILE_PATH)

    def __init__(self, type, *args, **kwargs):

        self.type = type

        try:
            self.code = self._responses_table.codes[type]
        except KeyError:
            raise MissingResponseCode('Missing response code in table of responses.')

        self.http_code = self.code['http_code']
        self.status = self.code['status']
        self.message = self.code.get('message')
        self.data = kwargs.get('data')

    def to_json(self):
        response = self.code.copy()

        if self.data:
            response['data'] = self.data

        response['code'] = response.pop('http_code')
        response['type'] = self.type

        return json.dumps(response)


def main():
    raise NotImplementedError


if __name__ == '__main__':
    main()
