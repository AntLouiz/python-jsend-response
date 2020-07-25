# PyJSend

PyJSend is a simply implementation of [JSend](https://github.com/omniti-labs/jsend).

JSend is a specification that lays down some rules for how JSON responses from web servers should be formatted. JSend focuses on application-level (as opposed to protocol- or transport-level) messaging which makes it ideal for use in REST-style applications and APIs.:

You'll have all kinds of different types of calls and responses. JSend separates responses into some basic types, and defines required and optional keys for each type:

<table>
<tr><th>Type</td><th>Description</th><th>Required Keys</th></tr>
<tr><td>success</td><td>All went well, and (usually) some data was returned.</td><td>status, data</td></tr>
<tr><td>failure</td><td>There was a problem with the data submitted, or some pre-condition of the API call wasn't satisfied</td><td>status, data</td></tr>
<tr><td>error</td><td>An error occurred in processing the request, i.e. an exception was thrown</td><td>status, message</td></tr>
</table>

## Some requirements to construct a valid response

PyJSend uses an file called **responses_table.json** to store the responses,
follow the requirements above to create an valid response.

* All the response code name must be in camel case.
* The status must be success, failure or error.
* The http_code must exist in the valid http codes.
* If the response have data, it must be an empty dict.
* If the response have message, it must be an string.

### Example of valid response

  {
    "SuccessfullLogin": {
      "http_code": 200,
      "status": "success",
      "data": {}
    }
  }

### Example of invalid response

  {
    "successfulllogin": {
      "http_code": 233,
      "status": "success",
      "data": {}
    }
  }

## Installation

### Using pip
To try out via pip, run:
```
$ pip install git+ssh://git@github.com/AntLouiz/pyjsend.git
```

## Usage

Import the **Response** class and select one of the response inserted in the response table:

```
>>> from pyjsend import Response

>>> response = Response('InvalidValueType')

>>> response.code
{'http_code': 400, 'status': 'failure', 'message': 'The value specified is invalid.'}

>>> response.http_code
400

>>> response.status
'failure'

>>> response.message
'The value specified is invalid.'

>>> response.to_json()
'{"status": "failure", "message": "The value specified is invalid.", "code": 400, "type": "InvalidValueType"}'
```
