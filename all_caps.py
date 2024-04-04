def all_caps_if_greater_than_ten_chars(word):
    return (word.upper() if len(word) > 10 else word)

print(all_caps_if_greater_than_ten_chars('hello world'))
print(all_caps_if_greater_than_ten_chars('goodbye'))