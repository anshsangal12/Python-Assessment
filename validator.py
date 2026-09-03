def validate_data(value, is_numeric)->bool:
    if value.strip() == "":
        return False
    if is_numeric:
        try:
            float(value)
            return True
        except ValueError:
            pass
    else:
        try:
            float(value)
            return False
        except ValueError:
            return True
    return False