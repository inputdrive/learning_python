def contains(big_string,little_string):
    if little_string in big_string:
        return True
    else:
        return False
print(contains("watermelon","melon"))

def common_letters(string_one, string_two):
    return list(set(string_one) & set(string_two))
print(common_letters("manhattan","san francisco"))