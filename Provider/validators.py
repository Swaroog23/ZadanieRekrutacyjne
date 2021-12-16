def validate_request_data(data):
    if data:
        for key, value in data.items():
            if not key.isnumeric():
                raise ValueError("Key must be numeric")
            elif value is None:
                raise ValueError("Value cannot be empty!")
    else:
        raise ValueError("Data cannot be empty!")


def validate_result_from_queue(result_list):
    for result in result_list:
        if result is not None:
            raise ValueError()


if __name__ == "__main__":
    pass