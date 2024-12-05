text = "this is a simple question return word with maximum number of characters"


words = text.split()


longest_word = max(words, key=len)

print(f"The word with the maximum number of characters is '{longest_word}' with {len(longest_word)} characters.")
