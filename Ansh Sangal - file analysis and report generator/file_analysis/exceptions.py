class InputValidationError(Exception):
    pass

def validate_input(value, message):
    if not value:
        raise InputValidationError(message)