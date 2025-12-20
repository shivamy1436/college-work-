def print_even_index_chars(text):
    even_chars = text[::2]
    print(f"Characters at even indices: {even_chars}")

my_string = "P y t h o n"
print(f"Original String: {my_string}")
print_even_index_chars(my_string)