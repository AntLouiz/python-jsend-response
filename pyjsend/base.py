import json


class ResponsesTable:
    def __init__(self, file_path):
        self.file = file_path
        self._load_responses_table()

    def _load_responses_table(self):
        with open(self.file, 'r') as file:
            response_table = file.read()
            response_table = json.loads(response_table)

            valid_codes = self.validate(response_table)

            if valid_codes:
                self.codes = valid_codes

    def validate(self, codes):
        raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == '__main__':
    main()
