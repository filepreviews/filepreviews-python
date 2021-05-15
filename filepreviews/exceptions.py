class FilePreviewsError(Exception):
    def __init__(self, message=None, http_body=None, http_status=None, json_body=None):
        super(FilePreviewsError, self).__init__(message)

        if http_body and hasattr(http_body, "decode"):
            try:
                http_body = http_body.decode("utf-8")
            except Exception:
                http_body = (
                    "<Could not decode body as utf-8. "
                    "Please report to support@blimp.io>"
                )

        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body


class APIError(FilePreviewsError):
    def __init__(self, message=None, http_body=None, http_status=None, json_body=None):

        if not message:
            message = (
                "Invalid response object from API: {body} "
                "(HTTP response code was {code})"
            ).format(body=http_body, code=http_status)

        super(APIError, self).__init__(message, http_body, http_status, json_body)


class InvalidRequestError(FilePreviewsError):
    def __init__(
        self, message, param, http_body=None, http_status=None, json_body=None
    ):
        super(InvalidRequestError, self).__init__(
            message, http_body, http_status, json_body
        )

        self.param = param


class AuthenticationError(FilePreviewsError):
    pass
