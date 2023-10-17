from datetime import datetime


class CustomExceptionBase(Exception):
    def __init__(self, status_code, error_type, error_message, fields=None):
        self.timestamp = datetime.now().isoformat()
        self.status = status_code
        self.error = error_type
        self.message = error_message
        self.fields = fields
        super().__init__(self.message)


class NotFoundError(CustomExceptionBase):
    def __init__(self, fields, item_id):
        error_message = f"Item with ID {item_id} not found"
        super().__init__(status_code=404, error_type="Not Found", error_message=error_message, fields=fields)


class BadRequestError(CustomExceptionBase):
    def __init__(self, fields, detail):
        error_message = f"Couldn't process the request: {detail}"
        super().__init__(status_code=400, error_type="Bad Request", error_message=error_message, fields=fields)


class UnsupportedMediaTypeError(CustomExceptionBase):
    def __init__(self):
        error_message = f"Media format of the requested data is not supported by the serve"
        super().__init__(status_code=415, error_type="Unsupported Media Type", error_message=error_message)


class CustomError(CustomExceptionBase):
    def __init__(self, status_code, error_type, error_message):
        super().__init__(status_code=status_code, error_type=error_type, error_message=error_message)


class CustomExceptionWithoutFields(Exception):
    def __init__(self, status_code, error_type, error_message):
        self.timestamp = datetime.now().isoformat()
        self.status = status_code
        self.error = error_type
        self.message = error_message
        super().__init__(self.message)


class CustomErrorWithoutFields(CustomExceptionWithoutFields):
    def __init__(self, status_code, error_type, error_message):
        super().__init__(status_code=status_code, error_type=error_type, error_message=error_message)