# step 1
def get_sum(a,b):
    return a + b

# step 2
def count_capital_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count

# step 3
def decode_string(text):
    result = ""
    text_lower = text.lower()

    for char in text_lower:
        count = 0
        for c in text_lower:
            if c == char:
                count += 1

        if count == 1:
            result += "("
        else:
            result += ")"

    return result

# step 4
def get_odd_count(numbers):
    count = 0
    for char in numbers:
        digit = int(char)
        if digit % 2 == 0 and digit != 0:
            count += 1
    return count

# step 5
def check_access(has_keycard, has_fingerprint, is_alarm, is_daylight):

    if is_alarm:
        return False

    if has_fingerprint:
        return True

    if has_keycard and is_daylight:
        return True

    return False