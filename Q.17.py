def find_longest_word(sentence):
    words = sentence.split()

    longest_word = max(words, key=len)

    longest_length = len(longest_word)

    return longest_word, longest_length

input_sentence = "The quick brown fox jumped over the lazy dog."

word, length = find_longest_word(input_sentence)

print(f"Original Sentence: '{input_sentence}'")
print(f"The longest word is: **{word}**")
print(f"Its length is: {length} characters")