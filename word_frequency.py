import re
from collections import Counter 
import matplotlib.pyplot as plt


def get_word_frequency(text):
  text = text.lower()
  text = re.sub(r"[^\w\s]", "", text)
  words = text.split()
  counts = Counter(words)
  return counts

with open("text.txt", "r") as f:
  text = f.read()

word_frequency = get_word_frequency(text)
sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
top_10_words = [i[0] for i in sorted_word_frequency[:10]]
top_10_counts = [i[1] for i in sorted_word_frequency[:10]]
plt.figure(figsize=(10,6))
plt.bar(top_10_words, top_10_counts)
plt.title("Top 10 Most Frequent Words in Text")
plt.xlabel("Words")
plt.ylabel("Counts")
plt.show()
