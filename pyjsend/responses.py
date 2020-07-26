import json


class BaseResponse:
    message = None
    data = None
    status = None
    http_code = None

    def to_json(self):
        response = {}

        if self.data:
            response['data'] = self.data
        else:
            response['message'] = self.message

        response['code'] = self.http_code
        response['type'] = self.__class__.__name__

        return json.dumps(response)


class SuccessResponse(BaseResponse):

    status = 'success'
    http_code = 200

    def __init__(self, data={}):
        self.data = data


class CreatedSuccessfullyResponse(SuccessResponse):
    http_code = 201


class FailureResponse(BaseResponse):
    status = 'failure'
    http_code = 400


class ErrorResponse(BaseResponse):
    status = 'error'
    http_code = 500


class BadResponse(FailureResponse):
    message = 'Bad Request'


class UnauthorizedResponse(FailureResponse):
    http_code = 401
    message = "Unauthorized"


class ForbiddenResponse(FailureResponse):
    http_code = 403
    message = 'Forbidden'


class NotFoundResponse(FailureResponse):
    http_code = 404
    message = "Not found"


class AccountAlreadyExistsResponse(BadResponse):
    message = 'User account already exists.'


class AccountDoesntMatchResponse(BadResponse):
    message = "Account doesn't match"


class AlreadyRevokedTokenResponse(BadResponse):
    message = "Token is already revoked"


class ValidationErrorResponse(BadResponse):
    message = "The fields specified are invalid."


class WrongDataResponse(BadResponse):
    message = "The data specified is invalid."


class EntityAlreadyExistsResponse(FailureResponse):
    http_code = 409
    message = "The specified entity already exists."


class NotAllowedResponse(ForbiddenResponse):
    message = "Not allowed to access this route."


class NotImplementedErrorResponse(ErrorResponse):
    http_code = 501
    message = "The requested operation is not implemented on the specified resource."


class UserAccountDoesntExistResponse(NotFoundResponse):
    message = "User account doesn't exist"
