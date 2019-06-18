class DataNotFoundException(Exception):
    def __init__(self, message='Data not found') -> None:
        super().__init__(message)
