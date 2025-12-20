def remove_duplicates_easy(text):
    unique_chars_set = set(text)

    result_string = "".join(unique_chars_set)

    return result_string

my_string = "programming"
output = remove_duplicates_easy(my_string)

print(f"Original String: {my_string}")
print(f"String with duplicates removed: {output}")

