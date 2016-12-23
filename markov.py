import random
import re

text = []

# We tokenize the corpus.
with open('corpus.txt') as fh:
    for line in fh:
        # We add a spaces between this characters so they are treated as words
        line = re.sub(r'([,.!?;:])', r' \1 ', line)
        # We remove all special characters.
        line = re.sub(r"[^a-zA-Z0-9,.!?;:’']", ' ', line)
        text += [word.lower().strip() for word in line.split() if word.strip() != ''] + ['\n']

markov_chain = {}

# We build the markov chain using bigrams as keys.
# Using bigrams instead of a single word gives more coherent texts.
for previous_word, current_word, next_word in zip(text, text[1:], text[2:]):
    markov_chain.setdefault((previous_word, current_word), []).append(next_word)

# We pick a random word to start the text.
previous_word, current_word = random.choice(list(markov_chain.keys()))
sentence = []

# We generate the text.
for _ in range(0, 20):
    sentence.append(current_word)
    if (previous_word, current_word) in markov_chain:
        previous_word, current_word = current_word, random.choice(markov_chain[(previous_word, current_word)])
    else:
        break

print(' '.join(sentence).replace('\n ', '\n'))
