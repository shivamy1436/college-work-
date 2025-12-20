def print_words_on_new_line(sentence):
   words_list = sentence.split()

   for word in words_list:
      print(word)

input_sentence = "Input a sentence and print each word on a new line."

print("--- Original Sentence ---")
print(input_sentence)
print("\n--- Words on New Lines ---")

print_words_on_new_line(input_sentence)
