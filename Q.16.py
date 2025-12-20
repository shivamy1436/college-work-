def count_char_occurrences(text, char_to_find):
    count = text.count(char_to_find)
    return count

my_string = "programming is fun"
target_char = 'g'

occurrences = count_char_occurrences(my_string, target_char)

print(f"The string is: '{my_string}'")
print(f"The character to find is: '{target_char}'")
print(f"The character '{target_char}' occurs {occurrences} times.")
