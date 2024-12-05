from collections import Counter
import re

text = "this is a simple python program that print most recursive word . this program is simple"

# Remove punctuation and convert to lowercase
cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

# Split the text into words
words = cleaned_text.split()

# Count the frequency of each word
word_count = Counter(words)

# Find the most common word and its frequency
most_common_word, frequency = word_count.most_common(1)[0]

print(f"The most frequent word is '{most_common_word}' which appears {frequency} times.")
