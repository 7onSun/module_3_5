def get_multiplied_digits(number) -> int:
    str_number = str(number)
    first = int(str_number[0])
    if len(str(number)) > 1:
        first *= get_multiplied_digits(int(str_number[1:]))
    return first


result = get_multiplied_digits(40203)
print(result)
