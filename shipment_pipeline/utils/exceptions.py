class ValidationError(Exception):
    pass


class DatabaseError(Exception):
    pass


class S3UploadError(Exception):
    pass


class ParsingError(Exception):
    pass